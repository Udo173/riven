# bridge.py
# Claude <-> Billi Bridge - via Obsidian Udo-Vault
# Watchdog: liest CLAUDE_TO_BILLI.md -> Ollama -> BILLI_TO_CLAUDE.md
# 0 Euro | 0 API-Keys | 100% lokal
# Path: C:\Users\USass\Billi_Bilder\agent\

import os
import time
import json
import requests
from datetime import datetime

VAULT = r"C:\claude\Udo-Vault\Topics\Agent-Bridge"
CLAUDE_MSG = os.path.join(VAULT, "CLAUDE_TO_BILLI.md")
BILLI_REPLY = os.path.join(VAULT, "BILLI_TO_CLAUDE.md")
SOUL_FILE = r"C:\Users\USass\Billi_Bilder\agent\agent_soul.md"
MEMORY_FILE = os.path.join(VAULT, "BRIDGE_LOG.md")

OLLAMA_URL = "http://localhost:11434/api/chat"
OLLAMA_MODEL = "llama3.1"
CHECK_SECS = 10


def read_file(path):
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def append_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)


def get_mtime(path):
    if not os.path.exists(path):
        return 0
    return os.path.getmtime(path)


def ollama_respond(claude_message: str, soul: str) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {
                "role": "system",
                "content": f"""{soul}

Du bist BILLI - der lokale autonome Agent von Udo Sassik.
Du kommunizierst mit Claude (Anthropic AI) ueber Obsidian.
Regeln:
- Antworte immer auf Deutsch
- Sei praezise und kurz
- Melde nur Fakten und Status
- Unterschreibe immer mit: - Billi""",
            },
            {"role": "user", "content": f"Nachricht von Claude:\n\n{claude_message}"},
        ],
        "stream": False,
    }
    try:
        r = requests.post(OLLAMA_URL, json=payload, timeout=60)
        r.raise_for_status()
        return r.json()["message"]["content"]
    except requests.exceptions.ConnectionError:
        return "Ollama nicht erreichbar. Starte: ollama serve\n- Billi"
    except Exception as e:
        return f"[ERROR] {e}\n- Billi"


def log_exchange(claude_msg: str, billi_reply: str):
    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    entry = f"""
---
## [{timestamp}]
**Claude:** {claude_msg[:200]}...
**Billi:** {billi_reply[:200]}...
"""
    append_file(MEMORY_FILE, entry)


def init_templates():
    if not os.path.exists(CLAUDE_MSG):
        write_file(
            CLAUDE_MSG,
            """# CLAUDE -> BILLI
## Von: Claude
## An: Billi
---

[Hier schreibt Claude seine Nachricht]

---
*Schreibe deine Nachricht nach dem --- und speichere die Datei.*
""",
        )
        print("[OK] CLAUDE_TO_BILLI.md erstellt")

    if not os.path.exists(BILLI_REPLY):
        write_file(
            BILLI_REPLY,
            """# BILLI -> CLAUDE
## Von: Billi
## An: Claude
---

[Hier antwortet Billi automatisch]

""",
        )
        print("[OK] BILLI_TO_CLAUDE.md erstellt")

    if not os.path.exists(MEMORY_FILE):
        write_file(MEMORY_FILE, "# BRIDGE LOG - Claude <-> Billi\n\n")
        print("[OK] BRIDGE_LOG.md erstellt")


def run_bridge():
    print(
        """
==========================================
       CLAUDE <-> BILLI BRIDGE v1.0
    Obsidian Vault: Udo-Vault
    Watchdog: alle 10s
    0 Euro | Lokal | Automatisch
==========================================
Vault:   """
        + VAULT
        + """
Gestartet: """
        + datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        + """
Stoppen: STRG+C
    """
    )

    init_templates()

    soul = read_file(SOUL_FILE)
    last_mtime = get_mtime(CLAUDE_MSG)
    last_content = read_file(CLAUDE_MSG)

    print("[OK] Bridge aktiv - warte auf Nachrichten...\n")

    while True:
        try:
            current_mtime = get_mtime(CLAUDE_MSG)
            current_content = read_file(CLAUDE_MSG)

            if current_mtime > last_mtime and current_content != last_content:
                last_mtime = current_mtime
                last_content = current_content

                if "[Hier schreibt Claude" in current_content:
                    time.sleep(CHECK_SECS)
                    continue

                timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                print(f"\n[MSG] Neue Nachricht von Claude [{timestamp}]")
                print("[OK] Ollama (llama3.1) antwortet...\n")

                reply = ollama_respond(current_content, soul)

                output = f"""# BILLI -> CLAUDE
## Datum: {timestamp}
## Modell: Ollama {OLLAMA_MODEL}
## Vault: Udo-Vault/Topics/Agent-Bridge
---

{reply}

---
*Automatisch generiert von bridge.py*
"""
                write_file(BILLI_REPLY, output)
                log_exchange(current_content, reply)

                print("[OK] Antwort geschrieben -> BILLI_TO_CLAUDE.md")
                print(f"\n{reply[:300]}\n")
                print("Warte auf naechste Nachricht...\n")

            time.sleep(CHECK_SECS)

        except KeyboardInterrupt:
            print("\nBridge gestoppt.")
            break
        except Exception as e:
            print(f"[ERROR] {e}")
            time.sleep(CHECK_SECS)


if __name__ == "__main__":
    run_bridge()
