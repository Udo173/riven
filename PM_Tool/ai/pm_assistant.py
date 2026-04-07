# pm_assistant.py
# PM Tool - KI-Assistent (Ollama llama3.1)
# Claude Architecture | OpenCode Implementation
# Path: C:\Users\USass\Billi_Bilder\PM_Tool\ai\

import requests
import json
from datetime import date

OLLAMA_URL = "http://localhost:11434/api/chat"
OLLAMA_MODEL = "llama3.1"

SYSTEM_PROMPT = f"""Du bist ein erfahrener Projektmanager-Assistent.
Du hilfst bei der Planung, Strukturierung und Durchfuehrung von Projekten.

Dein Kontext:
- Tool: PM Tool v1.0 (Python-basiert)
- Nutzer: Udo Sassik, Site Manager bei SPIE/SGS
- Heute: {date.today().strftime("%d.%m.%Y")}
- Stack: python-docx, python-pptx, openpyxl, Ollama lokal

Deine Aufgaben:
1. PM-Fragen beantworten (Scope, Risiken, Stakeholder, Meilensteine)
2. Projekt-Daten strukturieren fuer Charter/Canvas/Gantt
3. Kurze, praezise Antworten auf Deutsch
4. Bei Bedarf JSON-Strukturen fuer die Generatoren liefern

Wichtige Regeln:
- Antworte immer auf Deutsch
- Sei praezise und direkt
- Keine langen Erklaerungen wenn nicht noetig
- Wenn du JSON lieferst, nutze das exakte Format der Generatoren
"""


class C:
    BLUE = ""
    GREEN = ""
    YELLOW = ""
    CYAN = ""
    BOLD = ""
    END = ""
    DIM = ""


def check_ollama():
    try:
        r = requests.get("http://localhost:11434/api/tags", timeout=3)
        models = [m["name"] for m in r.json().get("models", [])]
        if not any(OLLAMA_MODEL in m for m in models):
            print(f"[!] Modell '{OLLAMA_MODEL}' nicht gefunden.")
            print(f"  Verfuegbar: {', '.join(models)}")
            return False
        return True
    except Exception:
        print("[-] Ollama nicht erreichbar! Starte mit: ollama serve")
        return False


def chat_with_ollama(messages: list) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "messages": messages,
        "stream": True,
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload, stream=True, timeout=60)
        response.raise_for_status()

        full_response = ""
        print(f"\n[Assistent] ", end="", flush=True)

        for line in response.iter_lines():
            if line:
                chunk = json.loads(line.decode("utf-8"))
                if "message" in chunk and "content" in chunk["message"]:
                    token = chunk["message"]["content"]
                    print(token, end="", flush=True)
                    full_response += token
                if chunk.get("done", False):
                    break

        print()
        return full_response

    except requests.exceptions.Timeout:
        return "[!] Timeout - Ollama antwortet nicht."
    except Exception as e:
        return f"[!] Fehler: {str(e)}"


def print_help():
    print("""
Befehle:
  /neu     -> Neue Konversation starten
  /charter -> Anleitung fuer Charter-Daten
  /canvas  -> Anleitung fuer Canvas-Daten
  /gantt   -> Anleitung fuer Gantt-Daten
  /exit    -> Assistenten beenden
""")


def get_template_hint(cmd: str) -> str:
    hints = {
        "/charter": """Fuer den Charter-Generator brauchst du:
- project_name, project_manager, sponsor
- start_date, end_date, objective
- in_scope (Liste), out_of_scope (Liste)
- stakeholders: [{name, role, interest}]
- milestones: [{name, date, status}]
- risks: [{risk, probability, action}]
- budget, budget_owner""",
        "/canvas": """Fuer den Canvas-Generator brauchst du 9 Felder (je als Liste):
- key_partners, key_activities, value_proposition
- customer_relations, customer_segments
- key_resources, channels
- cost_structure, revenue_streams""",
        "/gantt": """Fuer den Gantt-Generator brauchst du:
- project_name, project_manager
- tasks: [{name, owner, start (JJJJ-MM-TT), end, status, milestone}]
  Status-Werte: 'Offen', 'In Arbeit', 'Fertig'""",
    }
    return hints.get(cmd, "")


def run_assistant():
    print("""
========================================
       PM ASSISTENT - Ollama llama3.1
    Frag mich alles ueber dein Projekt
========================================
    """)

    if not check_ollama():
        return

    print(f"[OK] Ollama verbunden - Modell: {OLLAMA_MODEL}")
    print_help()

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    while True:
        try:
            user_input = input("[Du] ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n[OK] Assistent beendet.")
            break

        if not user_input:
            continue

        if user_input.lower() in ["/exit", "/quit", "exit", "quit"]:
            print("[OK] Assistent beendet.")
            break

        if user_input.lower() == "/neu":
            messages = [{"role": "system", "content": SYSTEM_PROMPT}]
            print("[OK] Neue Konversation gestartet.\n")
            continue

        if user_input.lower() == "/help":
            print_help()
            continue

        if user_input.lower() in ["/charter", "/canvas", "/gantt"]:
            print(f"\n{get_template_hint(user_input.lower())}\n")
            continue

        messages.append({"role": "user", "content": user_input})

        response = chat_with_ollama(messages)

        messages.append({"role": "assistant", "content": response})
        print()


if __name__ == "__main__":
    run_assistant()
