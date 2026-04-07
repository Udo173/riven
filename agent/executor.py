# executor.py
# Ollama-Agent Stage 3 - Ausfuehrer
# Liest SOLUTIONS.md -> Fuehrt Aktionen aus
# 0 Euro | 0 API-Keys | 100% lokal
# Path: C:\Users\USass\Billi_Bilder\agent\

import os
import subprocess
import sys
from datetime import datetime

BASE = r"C:\Users\USass\Billi_Bilder"
SOLUTIONS = os.path.join(BASE, "SHARED_BRAIN", "SOLUTIONS.md")
MEMORY = os.path.join(BASE, "SHARED_BRAIN", "MEMORY.md")
EXECUTOR_LOG = os.path.join(BASE, "agent", "EXECUTOR_LOG.md")


def log(msg):
    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    entry = f"[{timestamp}] {msg}\n"
    with open(EXECUTOR_LOG, "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"[EXEC] {msg}")


def read_solutions():
    if not os.path.exists(SOLUTIONS):
        return []
    with open(SOLUTIONS, "r", encoding="utf-8") as f:
        content = f.read()
    return content


def parse_tasks(content):
    """Extrahiert Aufgaben aus SOLUTIONS.md"""
    tasks = []

    # Suche nach losungen
    if "Loesungsvorschlag" in content or "Loesung" in content or "Loesung:" in content:
        tasks.append(
            {
                "type": "review",
                "desc": "Neue Loesungen gefunden - bitte manuell pruefen",
            }
        )

    if "Fehler" in content or "Error" in content or "ERROR" in content:
        tasks.append(
            {"type": "error", "desc": "Fehler erkannt - manuelle Pruefung noetig"}
        )

    if not tasks:
        tasks.append({"type": "ok", "desc": "Keine Aktionen erforderlich - alles OK"})

    return tasks


def execute_task(task):
    """Fuehrt eine Aufgabe aus"""
    t_type = task.get("type", "unknown")
    desc = task.get("desc", "")

    log(f"Fuehre aus: {t_type}")
    log(f"Beschreibung: {desc}")

    if t_type == "ok":
        log("Status: System OK - keine Aktion")
        return True

    elif t_type == "review":
        log("Status: Manuelle Pruefung empfohlen")
        return True

    elif t_type == "error":
        log("Status: FEHLER - menschliche Intervention noetig")
        return True

    return False


def write_report(tasks_executed, success):
    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    report = f"""
---
## EXECUTOR-REPORT [{timestamp}]
- Aufgaben ausgefuehrt: {len(tasks_executed)}
- Erfolgreich: {success}
- Naechste Pruefung: Nach SOLUTIONS.md Update
---
"""
    with open(MEMORY, "a", encoding="utf-8") as f:
        f.write(report)


def run():
    print("""
==========================================
       EXECUTOR v1.0 - Stage 3
    Liest SOLUTIONS.md -> Fuehrt aus
==========================================
    """)

    log("=== EXECUTOR GESTARTET ===")

    # SOLUTIONS.md lesen
    content = read_solutions()

    if not content.strip():
        log("SOLUTIONS.md ist leer - nichts zu tun")
        return

    # Aufgaben extrahieren
    tasks = parse_tasks(content)
    log(f"{len(tasks)} Aufgaben gefunden")

    # Aufgaben ausfuehren
    executed = []
    success = True

    for task in tasks:
        result = execute_task(task)
        executed.append(task)
        if not result:
            success = False

    # Report schreiben
    write_report(executed, success)

    log("=== EXECUTOR BEENDET ===")
    print("\n[OK] Ausfuehrung abgeschlossen")
    print("[OK] Report geschrieben -> MEMORY.md")


if __name__ == "__main__":
    run()
