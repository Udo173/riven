# denker.py
# Ollama-Agent Stage 2 - Denker
# Liest MEMORY.md -> Analysiert mit Ollama -> Schreibt SOLUTIONS.md
# 0 Euro | 0 API-Keys | 100% lokal
# Path: C:\Users\USass\Billi_Bilder\agent\

import os
import requests
import json
from datetime import datetime

BASE = r"C:\Users\USass\Billi_Bilder"
MEMORY_FILE = os.path.join(BASE, "SHARED_BRAIN", "MEMORY.md")
SOUL_FILE = os.path.join(BASE, "agent", "agent_soul.md")
SOLUTIONS = os.path.join(BASE, "SHARED_BRAIN", "SOLUTIONS.md")

OLLAMA_URL = "http://localhost:11434/api/chat"
OLLAMA_MODEL = "llama3.1"


def read_memory(path: str) -> str:
    if not os.path.exists(path):
        print("[ERROR] MEMORY.md nicht gefunden")
        return ""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    print(f"[OK] MEMORY.md gelesen - {len(content)} Zeichen")
    return content


def read_soul(path: str) -> str:
    if not os.path.exists(path):
        return "Du bist ein praeziser Assistent."
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def analyse_with_ollama(memory_content: str, soul: str) -> str:
    if not memory_content.strip():
        return "Kein MEMORY.md Inhalt zum Analysieren."

    system_prompt = f"""{soul}

Du bist der DENKER - Stage 2 des autonomen Agenten.
Deine Aufgabe:
1. Lies den Waechter-Report aus MEMORY.md
2. Identifiziere alle Fehler und Warnungen
3. Erstelle konkrete Loesungsvorschlaege
4. Antworte NUR auf Deutsch
5. Sei praezise und direkt
"""

    user_prompt = f"""Analysiere diesen Waechter-Report:

{memory_content}

Antworte im Format:
## DENKER-ANALYSE
### Gefundene Probleme:
- [Liste]
### Loesungsvorschlaege:
- [Konkrete Schritte]
### Prioritaet:
- HOCH / MITTEL / NIEDRIG
"""

    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "stream": True,
    }

    print("\nOllama analysiert...\n")
    full_response = ""

    try:
        response = requests.post(OLLAMA_URL, json=payload, stream=True, timeout=120)
        response.raise_for_status()

        for line in response.iter_lines():
            if line:
                chunk = json.loads(line.decode("utf-8"))
                if "message" in chunk and "content" in chunk["message"]:
                    token = chunk["message"]["content"]
                    print(token, end="", flush=True)
                    full_response += token
                if chunk.get("done", False):
                    break

        print("\n")
        return full_response

    except requests.exceptions.ConnectionError:
        msg = "[ERROR] Ollama nicht erreichbar - starte: ollama serve"
        print(msg)
        return msg
    except Exception as e:
        msg = f"[ERROR] {str(e)}"
        print(msg)
        return msg


def write_solutions(path: str, analysis: str):
    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M")

    entry = f"""
---
## DENKER-REPORT [{timestamp}]
{analysis}
---
"""
    try:
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                f.write("# SOLUTIONS.md - Denker-Analysen\n\n")

        with open(path, "a", encoding="utf-8") as f:
            f.write(entry)

        print(f"[OK] SOLUTIONS.md geschrieben")

    except Exception as e:
        print(f"[ERROR] SOLUTIONS.md: {e}")


def billi_bridge_status():
    bridge_file = os.path.join(BASE, "SHARED_BRAIN", "BILLI_STATUS.md")
    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M")

    files_to_check = {
        "MEMORY.md": MEMORY_FILE,
        "SOLUTIONS.md": SOLUTIONS,
        "RULES.md": os.path.join(BASE, "SHARED_BRAIN", "RULES.md"),
        "agent_soul.md": SOUL_FILE,
    }

    status_lines = [f"# BILLI STATUS - {timestamp}\n"]
    for name, path in files_to_check.items():
        exists = os.path.exists(path)
        icon = "[OK]" if exists else "[ERROR]"
        size = f"{os.path.getsize(path)} Bytes" if exists else "fehlt"
        status_lines.append(f"- {icon} {name}: {size}")

    status_lines.append(f"\n## Aktiver Agent: Denker (Stage 2)")
    status_lines.append(f"## Modell: Ollama {OLLAMA_MODEL}")
    status_lines.append(f"## Kosten: 0 Euro")

    content = "\n".join(status_lines)

    with open(bridge_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n[OK] BILLI_STATUS.md aktualisiert")
    print(content)


def run_denker():
    print(
        """
==========================================
       DENKER v1.0 - Stage 2
   MEMORY.md -> Ollama -> SOLUTIONS.md
          0 Euro | 0 API-Keys
==========================================
Gestartet: """
        + datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    )

    print("=== LESEN ===")
    memory = read_memory(MEMORY_FILE)
    soul = read_soul(SOUL_FILE)
    print()

    print("=== ANALYSE ===")
    analysis = analyse_with_ollama(memory, soul)

    print("=== SCHREIBEN ===")
    write_solutions(SOLUTIONS, analysis)
    print()

    print("=== BILLI-BRIDGE ===")
    billi_bridge_status()

    print("\n=== DENKER FERTIG ===")


if __name__ == "__main__":
    run_denker()
