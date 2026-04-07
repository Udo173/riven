# agent_loop.py
# PM Tool - Waechter Haupt-Loop (Plan->Act->Observe->Refine)
# Claude Architecture | OpenCode Implementation
# Path: C:\Users\USass\Billi_Bilder\agent\

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))
from agent_tools import (
    check_files,
    check_excel_folder,
    write_memory,
    load_tasks,
    OK,
    WARN,
    ERROR,
)

BASE = r"C:\Users\USass\Billi_Bilder"
TASKS_FILE = os.path.join(BASE, "agent", "agent_tasks.json")
MEMORY_FILE = os.path.join(BASE, "SHARED_BRAIN", "MEMORY.md")


def print_header():
    print(
        """
==========================================
       WAECHTER v1.0 - Stage 1
    Plan -> Act -> Observe -> Refine
==========================================
Gestartet: """
        + datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    )


def plan(tasks: list) -> list:
    print("=== PLAN ===")
    priority_order = {"HOCH": 0, "MITTEL": 1, "NIEDRIG": 2}
    sorted_tasks = sorted(
        tasks, key=lambda t: priority_order.get(t.get("priority", "MITTEL"), 1)
    )
    for t in sorted_tasks:
        print(f"  [{t['priority']}] {t['id']} - {t['name']}")
    print()
    return sorted_tasks


def act(tasks: list) -> dict:
    print("=== ACT ===")
    all_results = {}
    tasks_run = 0

    for task in tasks:
        task_id = task.get("id", "?")
        task_name = task.get("name", "?")
        task_type = task.get("type", "")

        print(f"\n  -> {task_id}: {task_name}")

        if task_type == "file_check":
            results = check_files(task.get("targets", []))
            all_results.update(results)
            tasks_run += 1

        elif task_type == "excel_check":
            for folder in task.get("targets", []):
                result = check_excel_folder(
                    folder,
                    task.get("expected_extensions", [".xlsx"]),
                    task.get("min_files", 1),
                )
                all_results[folder] = result["status"]
            tasks_run += 1

        elif task_type == "memory_write":
            tasks_run += 1
            print(f"  -> Memory-Write in REFINE Phase")

    print()
    return {"results": all_results, "tasks_run": tasks_run}


def observe(report: dict) -> str:
    print("=== OBSERVE ===")

    results = report.get("results", {})
    errors = [k for k, v in results.items() if ERROR in str(v)]
    warnings = [k for k, v in results.items() if WARN in str(v)]
    ok_count = len(results) - len(errors) - len(warnings)

    print(f"  Geprueft:   {len(results)} Eintraege")
    print(f"  [OK]        {ok_count}")
    print(f"  [WARN]      {len(warnings)}")
    print(f"  [ERROR]     {len(errors)}")

    if errors:
        overall = "FEHLER"
        print(f"\n  -> Status: FEHLER - Manuelle Pruefung noetig")
    elif warnings:
        overall = "WARNUNG"
        print(f"\n  -> Status: WARNUNG - Pruefe fehlende Dateien")
    else:
        overall = "OK"
        print(f"\n  -> Status: ALLES OK")

    print()
    return overall


def refine(report: dict):
    print("=== REFINE ===")
    write_memory(MEMORY_FILE, report)
    print()


def run():
    print_header()

    print("=== LOAD TASKS ===")
    tasks = load_tasks(TASKS_FILE)
    if not tasks:
        print("[ERROR] Keine Tasks - Abbruch.")
        return
    print()

    planned_tasks = plan(tasks)
    report = act(planned_tasks)
    overall = observe(report)
    report["overall"] = overall
    refine(report)

    print("=== WAECHTER FERTIG ===")
    print(f"Report gespeichert -> MEMORY.md")
    print(f"Status: {overall}\n")


if __name__ == "__main__":
    run()
