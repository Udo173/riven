# thinker_loop.py
# PM Tool - Denker Haupt-Loop (Stage 2)
# Path: C:\Users\USass\Billi_Bilder\agent\

import os
import sys
import json
import requests
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))
from thinker_tools import (
    read_memory,
    load_rules,
    write_solutions,
    build_analysis_prompt,
    prepare_handover,
    OK,
    WARN,
    ERROR,
)

OLLAMA_URL = "http://localhost:11434/api/chat"
OLLAMA_MODEL = "llama3.1"


def print_header():
    print(
        """
==========================================
       DENKER v1.0 - Stage 2
    Analysieren -> Denken -> Loesen
==========================================
Gestartet: """
        + datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    )


def analyze_with_ollama(prompt: str) -> list:
    """Analysiert Fehler mit Ollama llama3.1"""
    print(f"\n  -> Ollama llama3.1 wird befragt...")

    messages = [{"role": "user", "content": prompt}]

    try:
        response = requests.post(
            OLLAMA_URL, json={"model": OLLAMA_MODEL, "messages": messages}, timeout=60
        )

        if response.status_code == 200:
            result = response.json()
            content = result.get("message", {}).get("content", "")

            # JSON aus Response extrahieren
            json_match = None
            for start in range(len(content)):
                if content[start:].strip().startswith("{"):
                    try:
                        json_match = json.loads(content[start:])
                        break
                    except:
                        continue

            if json_match and "solutions" in json_match:
                print(f"  {OK} {len(json_match['solutions'])} Loesungen gefunden")
                return json_match["solutions"]
            else:
                print(f"  {WARN} Keine Loesungen in Ollama-Antwort")
                return []
        else:
            print(f"  {ERROR} Ollama Fehler: {response.status_code}")
            return []

    except requests.exceptions.ConnectionError:
        print(f"  {ERROR} Ollama nicht erreichbar (ollama serve?)")
        return []
    except Exception as e:
        print(f"  {ERROR} Analysefehler: {e}")
        return []


def run():
    print_header()

    print("\n=== PHASE 1: MEMORY ANALYSIEREN ===")
    memory_data = read_memory()

    if memory_data["status"] != OK:
        print(f"\n{ERROR} MEMORY.md konnte nicht gelesen werden")
        return

    # Pruefen ob ueberhaupt etwas zu analysieren
    if not memory_data["errors"] and not memory_data["warnings"]:
        print(f"\n{OK} Keine Fehler oder Warnungen gefunden")
        print("  -> Nichts zu analysieren")
        write_solutions([])
        return

    print("\n=== PHASE 2: REGELN LADEN ===")
    rules = load_rules()
    print(f"  {OK} RULES.md geladen")

    print("\n=== PHASE 3: OLLAMA ANALYSE ===")
    prompt = build_analysis_prompt(memory_data, rules)
    solutions = analyze_with_ollama(prompt)

    print("\n=== PHASE 4: LOESUNGEN DOKUMENTIEREN ===")
    if solutions:
        write_solutions(solutions)

        print("\n=== PHASE 5: UEBERGABE VORBEREITEN ===")
        handover = prepare_handover(solutions)
        print(handover)
    else:
        print(f"\n{OK} Keine Loesungen erforderlich")
        write_solutions([])

    print("\n=== DENKER FERTIG ===")
    print(f"Loesungen: SOLUTIONS.md")
    print(f"Naechster Schritt: Stage 3 (Ausfuehrer)\n")


if __name__ == "__main__":
    run()
