# main.py
# PM Tool - CLI Einstiegspunkt
# Claude Architecture | OpenCode Implementation
# Path: C:\Users\USass\Billi_Bilder\PM_Tool\

import sys
import os
from datetime import date

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "core"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "ai"))
from charter_generator import create_project_charter
from canvas_generator import create_canvas
from gantt_generator import create_gantt
from pm_assistant import run_assistant


class C:
    BLUE = ""
    GREEN = ""
    YELLOW = ""
    RED = ""
    BOLD = ""
    END = ""


BASE_PATH = r"C:\Users\USass\Billi_Bilder\PM_Tool"


def ask(prompt, default=""):
    val = input(f"  {prompt} [{default}]: ").strip()
    return val if val else default


def ask_list(prompt):
    print(f"  {prompt} (leer lassen zum Beenden):")
    items = []
    while True:
        item = input("    -> ").strip()
        if not item:
            break
        items.append(item)
    return items if items else ["-"]


def collect_base_data():
    print("\n=== PROJEKT-INFORMATIONEN ===")
    return {
        "project_name": ask("Projektname", "Mein Projekt"),
        "project_manager": ask("Projektleiter", "Udo Sassik"),
        "sponsor": ask("Auftraggeber", "-"),
        "start_date": ask("Startdatum", date.today().strftime("%d.%m.%Y")),
        "end_date": ask("Enddatum", "-"),
        "version": ask("Version", "1.0"),
        "status": ask("Status", "In Planung"),
        "budget": ask("Budget", "0 Euro"),
        "budget_owner": ask("Budget-Owner", "Udo Sassik"),
    }


def collect_charter_data(base):
    data = dict(base)
    print("\n=== CHARTER-DETAILS ===")
    data["objective"] = ask("Projektziel")
    data["in_scope"] = ask_list("Im Scope")
    data["out_of_scope"] = ask_list("Ausserhalb des Scope")

    print("\n  Stakeholder eingeben:")
    stakeholders = []
    while True:
        name = input("    Name (leer = fertig): ").strip()
        if not name:
            break
        role = input("    Rolle: ").strip()
        interest = input("    Interesse: ").strip()
        stakeholders.append({"name": name, "role": role, "interest": interest})
    data["stakeholders"] = stakeholders or [{"name": "-", "role": "-", "interest": "-"}]

    print("\n  Meilensteine eingeben:")
    milestones = []
    while True:
        name = input("    Meilenstein (leer = fertig): ").strip()
        if not name:
            break
        ms_date = input("    Datum (TT.MM.JJJJ): ").strip()
        status = input("    Status [Offen]: ").strip() or "Offen"
        milestones.append({"name": name, "date": ms_date, "status": status})
    data["milestones"] = milestones or [{"name": "-", "date": "-", "status": "Offen"}]

    print("\n  Risiken eingeben:")
    risks = []
    while True:
        risk = input("    Risiko (leer = fertig): ").strip()
        if not risk:
            break
        prob = input("    Wahrscheinlichkeit [Mittel]: ").strip() or "Mittel"
        action = input("    Massnahme: ").strip()
        risks.append({"risk": risk, "probability": prob, "action": action})
    data["risks"] = risks or [{"risk": "-", "probability": "-", "action": "-"}]
    return data


def collect_canvas_data(base):
    data = dict(base)
    print("\n=== CANVAS-FELDER ===")
    fields = [
        ("key_partners", "Key Partners"),
        ("key_activities", "Key Activities"),
        ("value_proposition", "Value Proposition"),
        ("customer_relations", "Customer Relations"),
        ("customer_segments", "Customer Segments"),
        ("key_resources", "Key Resources"),
        ("channels", "Channels"),
        ("cost_structure", "Cost Structure"),
        ("revenue_streams", "Revenue Streams"),
    ]
    for key, label in fields:
        data[key] = ask_list(label)
    return data


def collect_gantt_data(base):
    data = dict(base)
    print("\n=== AUFGABEN (JJJJ-MM-TT Format) ===")
    tasks = []
    while True:
        name = input("  Aufgabe (leer = fertig): ").strip()
        if not name:
            break
        owner = input("  Verantwortlich: ").strip() or "-"
        start = input("  Start (JJJJ-MM-TT): ").strip()
        end = input("  Ende  (JJJJ-MM-TT): ").strip()
        status = input("  Status [Offen]: ").strip() or "Offen"
        ms = input("  Meilenstein? (j/n) [n]: ").strip().lower() == "j"
        tasks.append(
            {
                "name": name,
                "owner": owner,
                "start": start,
                "end": end,
                "status": status,
                "milestone": ms,
            }
        )
    data["tasks"] = tasks
    return data


def print_header():
    print("""
========================================
       PM TOOL v1.0  by Udo Sassik
  Claude Architecture | OpenCode Build
========================================
    """)


def print_menu():
    print("Was moechtest du erstellen?")
    print("  [1] Project Charter (.docx)")
    print("  [2] Business Model Canvas (.pptx)")
    print("  [3] Gantt Chart (.xlsx)")
    print("  [4] ALLES ERSTELLEN (Charter + Canvas + Gantt)")
    print("  [5] KI-Assistent starten (Ollama llama3.1)")
    print("  [0] Beenden")
    return input("\nAuswahl: ").strip()


def make_output_path(project_name, suffix, ext):
    safe = project_name.replace(" ", "_")
    return os.path.join(BASE_PATH, f"{safe}_{suffix}.{ext}")


def main():
    print_header()

    while True:
        choice = print_menu()

        if choice == "0":
            print("\nTschuess! PM Tool beendet.\n")
            break

        elif choice == "1":
            base = collect_base_data()
            data = collect_charter_data(base)
            path = make_output_path(base["project_name"], "Charter", "docx")
            create_project_charter(data, path)
            print("[OK] Charter fertig!\n")

        elif choice == "2":
            base = collect_base_data()
            data = collect_canvas_data(base)
            path = make_output_path(base["project_name"], "Canvas", "pptx")
            create_canvas(data, path)
            print("[OK] Canvas fertig!\n")

        elif choice == "3":
            base = collect_base_data()
            data = collect_gantt_data(base)
            path = make_output_path(base["project_name"], "Gantt", "xlsx")
            create_gantt(data, path)
            print("[OK] Gantt fertig!\n")

        elif choice == "4":
            print("\nAlle 3 Dokumente werden erstellt...")
            base = collect_base_data()

            data_c = collect_charter_data(dict(base))
            create_project_charter(
                data_c, make_output_path(base["project_name"], "Charter", "docx")
            )

            data_v = collect_canvas_data(dict(base))
            create_canvas(
                data_v, make_output_path(base["project_name"], "Canvas", "pptx")
            )

            data_g = collect_gantt_data(dict(base))
            create_gantt(
                data_g, make_output_path(base["project_name"], "Gantt", "xlsx")
            )

            print("\n[OK] ALLE 3 DOKUMENTE ERSTELLT!\n")

        elif choice == "5":
            sys.path.insert(0, os.path.join(os.path.dirname(__file__), "ai"))
            from pm_assistant import run_assistant

            run_assistant()

        else:
            print("Ungueltige Auswahl.\n")


if __name__ == "__main__":
    main()
