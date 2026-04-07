# agent_tools.py
# PM Tool - Waechter Tool-Funktionen
# Claude Architecture | OpenCode Implementation
# Path: C:\Users\USass\Billi_Bilder\agent\

import os
import json
import glob
from datetime import datetime

OK = "[OK]"
WARN = "[WARN]"
ERROR = "[ERROR]"


def check_files(targets: list) -> dict:
    results = {}
    for path in targets:
        if os.path.exists(path):
            results[path] = OK
            print(f"  {OK} - {os.path.basename(path)}")
        else:
            results[path] = ERROR
            print(f"  {ERROR} - {path}")
    return results


def check_excel_folder(folder: str, extensions: list, min_files: int = 1) -> dict:
    result = {"status": ERROR, "files_found": 0, "files": []}

    if not os.path.exists(folder):
        print(f"  {ERROR} - Ordner nicht gefunden: {folder}")
        return result

    found = []
    for ext in extensions:
        found += glob.glob(os.path.join(folder, f"*{ext}"))
        found += glob.glob(os.path.join(folder, f"**/*{ext}"), recursive=True)

    found = list(set(found))
    result["files_found"] = len(found)
    result["files"] = [os.path.basename(f) for f in found]

    if len(found) >= min_files:
        result["status"] = OK
        print(f"  {OK} - {len(found)} Excel-Datei(en) gefunden:")
        for f in result["files"]:
            print(f"    -> {f}")
    else:
        result["status"] = WARN
        print(f"  {WARN} - Nur {len(found)} Datei(en), erwartet: {min_files}")

    return result


def write_memory(memory_path: str, report: dict) -> bool:
    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M")

    errors = [k for k, v in report.get("results", {}).items() if ERROR in str(v)]
    warnings = [k for k, v in report.get("results", {}).items() if WARN in str(v)]

    if errors:
        overall = "[ERROR]"
    elif warnings:
        overall = "[WARN]"
    else:
        overall = "[OK]"

    entry = f"""
## WAECHTER-REPORT [{timestamp}]
- **Status:** {overall}
- **Gepruefte Tasks:** {report.get("tasks_run", 0)}
- **Fehler:** {len(errors)}
- **Warnungen:** {len(warnings)}
"""
    if errors:
        entry += "- **Fehler-Details:**\n"
        for e in errors:
            entry += f"  - {os.path.basename(e)}\n"

    if warnings:
        entry += "- **Warn-Details:**\n"
        for w in warnings:
            entry += f"  - {os.path.basename(w)}\n"

    entry += f"- **Naechste Pruefung:** Manuell oder Task Scheduler\n"
    entry += "---\n"

    try:
        if not os.path.exists(memory_path):
            os.makedirs(os.path.dirname(memory_path), exist_ok=True)
            with open(memory_path, "w", encoding="utf-8") as f:
                f.write("# MEMORY.md - Waechter-Reports\n\n")

        with open(memory_path, "a", encoding="utf-8") as f:
            f.write(entry)

        print(f"\n  [OK] Report -> MEMORY.md geschrieben")
        return True

    except Exception as e:
        print(f"\n  {ERROR} MEMORY.md Fehler: {e}")
        return False


def load_tasks(tasks_path: str) -> list:
    try:
        with open(tasks_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        tasks = [t for t in data.get("tasks", []) if t.get("status") == "aktiv"]
        print(f"  -> {len(tasks)} aktive Tasks geladen")
        return tasks
    except Exception as e:
        print(f"  {ERROR} Tasks nicht ladbar: {e}")
        return []
