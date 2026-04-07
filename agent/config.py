# config.py
# Zentraler Konfigurations-Datei
# Alle Pfade und Einstellungen an einem Ort

import os

# === BASIS-ORDNER ===
BASE = r"C:\Users\USass\Billi_Bilder"

# === AGENT ===
AGENT_DIR = os.path.join(BASE, "agent")

# === SHARED BRAIN ===
SHARED_BRAIN = os.path.join(BASE, "SHARED_BRAIN")
MEMORY = os.path.join(SHARED_BRAIN, "MEMORY.md")
SOLUTIONS = os.path.join(SHARED_BRAIN, "SOLUTIONS.md")
BILLI_STATUS = os.path.join(SHARED_BRAIN, "BILLI_STATUS.md")
RULES = os.path.join(SHARED_BRAIN, "RULES.md")

# === OBSIDIAN VAULT ===
VAULT = r"C:\claude\Udo-Vault\Topics\Agent-Bridge"
TO_BILLI = os.path.join(VAULT, "CLAUDE_TO_BILLI.md")
FROM_BILLI = os.path.join(VAULT, "BILLI_TO_CLAUDE.md")
BRIDGE_LOG = os.path.join(VAULT, "BRIDGE_LOG.md")

# === PM TOOL ===
PM_TOOL = os.path.join(BASE, "PM_Tool")
PM_CORE = os.path.join(PM_TOOL, "core")
PM_AI = os.path.join(PM_TOOL, "ai")

# === OLLAMA ===
OLLAMA_URL = "http://localhost:11434/api/chat"
OLLAMA_MODEL = "llama3.1"

# === CHECK-INTERVAL (Sekunden) ===
CHECK_SECS = 10

# === AGENT SOUL ===
AGENT_SOUL = os.path.join(AGENT_DIR, "agent_soul.md")
THINKER_SOUL = os.path.join(AGENT_DIR, "thinker_soul.md")

# === TASKS ===
AGENT_TASKS = os.path.join(AGENT_DIR, "agent_tasks.json")


def get_all_paths():
    """Gibt alle wichtigen Pfade als Dict zurueck"""
    return {
        "BASE": BASE,
        "AGENT_DIR": AGENT_DIR,
        "SHARED_BRAIN": SHARED_BRAIN,
        "MEMORY": MEMORY,
        "SOLUTIONS": SOLUTIONS,
        "VAULT": VAULT,
        "PM_TOOL": PM_TOOL,
        "OLLAMA_MODEL": OLLAMA_MODEL,
    }


def check_paths():
    """Prueft ob alle Pfade existieren"""
    paths = get_all_paths()
    missing = []

    for name, path in paths.items():
        if name.startswith("OLLAMA"):
            continue
        if not os.path.exists(path):
            missing.append(f"{name}: {path}")

    return missing


if __name__ == "__main__":
    print("=== KONFIGURATION ===")
    for name, path in get_all_paths().items():
        print(f"{name}: {path}")

    print("\n=== PRUEFUNG ===")
    missing = check_paths()
    if missing:
        print("FEHLT:")
        for m in missing:
            print(f"  - {m}")
    else:
        print("Alle Pfade OK")
