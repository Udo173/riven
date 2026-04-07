# billi_mcp_server.py
# Lokaler MCP Server - Claude <-> Billi Bridge
# 0 Euro | 0 API-Keys | Claude Desktop Integration
# Path: C:\Users\USass\Billi_Bilder\agent\

from fastmcp import FastMCP
from datetime import datetime
import os

VAULT = r"C:\claude\Udo-Vault\Topics\Agent-Bridge"
TO_BILLI = os.path.join(VAULT, "CLAUDE_TO_BILLI.md")
FROM_BILLI = os.path.join(VAULT, "BILLI_TO_CLAUDE.md")

mcp = FastMCP("Billi Bridge")


@mcp.tool()
def get_billi_thoughts() -> str:
    """Liest Billis letzte Nachricht aus dem Obsidian Vault."""
    if not os.path.exists(FROM_BILLI):
        return "Keine Nachricht von Billi vorhanden."
    with open(FROM_BILLI, "r", encoding="utf-8") as f:
        return f.read()


@mcp.tool()
def send_to_billi(message: str) -> str:
    """Schreibt Claudes Nachricht in den Obsidian Vault fuer Billi."""
    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    content = f"""# CLAUDE -> BILLI
## Datum: {timestamp}
---

{message}

---
"""
    os.makedirs(VAULT, exist_ok=True)
    with open(TO_BILLI, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Nachricht an Billi gesendet. Antwort in ~10 Sekunden."


@mcp.tool()
def get_bridge_status() -> str:
    """Zeigt Status aller Bridge-Dateien."""
    files = {
        "CLAUDE_TO_BILLI.md": TO_BILLI,
        "BILLI_TO_CLAUDE.md": FROM_BILLI,
    }
    lines = [f"# Bridge Status - {datetime.now().strftime('%d.%m.%Y %H:%M')}"]
    for name, path in files.items():
        exists = os.path.exists(path)
        size = f"{os.path.getsize(path)} Bytes" if exists else "fehlt"
        lines.append(f"- {'OK' if exists else 'FEHLT'} {name}: {size}")
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
