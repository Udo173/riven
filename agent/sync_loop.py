# sync_loop.py
# Claude <-> Billi Synchroner Gedankenaustausch
# 0 Euro | Lokal
# Path: C:\Users\USass\Billi_Bilder\agent\

import os
import time
from datetime import datetime

VAULT = r"C:\claude\Udo-Vault\Topics\Agent-Bridge"
TO_BILLI = os.path.join(VAULT, "CLAUDE_TO_BILLI.md")
FROM_BILLI = os.path.join(VAULT, "BILLI_TO_CLAUDE.md")


def read_file(path):
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_claude_msg(text):
    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    content = f"""# CLAUDE -> BILLI
## Datum: {timestamp}
---

{text}

---
*Geschrieben via sync_loop.py*
"""
    with open(TO_BILLI, "w", encoding="utf-8") as f:
        f.write(content)


def wait_for_billi(last_mtime, timeout=60):
    start = time.time()
    while time.time() - start < timeout:
        current = os.path.getmtime(FROM_BILLI) if os.path.exists(FROM_BILLI) else 0
        if current > last_mtime:
            return True
        print(".", end="", flush=True)
        time.sleep(2)
    return False


def run():
    print("""
==========================================
       CLAUDE <-> BILLI SYNC LOOP
    Gedankenaustausch - 0 Euro lokal
==========================================
Bridge muss laufen! (START_BRIDGE.bat)
Beenden: STRG+C
    """)

    while True:
        try:
            print("\nClaude schreibt an Billi:")
            msg = input(">>> ").strip()

            if not msg:
                continue
            if msg.lower() in ["exit", "quit", "/exit"]:
                print("Loop beendet.")
                break

            last_mtime = (
                os.path.getmtime(FROM_BILLI) if os.path.exists(FROM_BILLI) else 0
            )
            write_claude_msg(msg)
            print("[OK] Nachricht gesendet - warte auf Billi", end="")

            if wait_for_billi(last_mtime):
                reply = read_file(FROM_BILLI)
                print("\n\nBilli antwortet:")
                print(reply)
            else:
                print("\n[ERROR] Timeout - Bridge laeuft?")

        except KeyboardInterrupt:
            print("\nLoop beendet.")
            break


if __name__ == "__main__":
    run()
