# AI Agent System - Udo Sassik

## Uebersicht

Ein vollstaendig lokales AI-Agent-System. Keine Cloud-Kosten. Keine API-Keys.

```
Kosten: 0 Euro
Stack: Ollama (lokal) + Python + Obsidian
Agenten: Billi (lokal) + Claude (Cloud, optional)
```

---

## Ordner-Struktur

```
Billi_Bilder/
├── agent/                    # AI Agent System
│   ├── bridge.py           # Watchdog - beobachtet Vault
│   ├── billi_mcp_server.py # MCP Server - Claude Desktop Verbindung
│   ├── sync_loop.py        # Synchroner Gedankenaustausch
│   ├── agent_loop.py       # Waechter Stage 1
│   ├── denker.py           # Denker Stage 2
│   ├── agent_tools.py       # Tool-Funktionen
│   ├── agent_soul.md       # Persoenlichkeit + Regeln
│   ├── agent_tasks.json    # Aufgaben-Queue
│   ├── START_ALL.bat       # Startet alles
│   ├── START_BRIDGE.bat    # Nur Bridge
│   └── BilliReader.html    # Vault Reader
│
├── PM_Tool/                # Project Management Tool
│   ├── core/               # Generator-Module
│   ├── ai/                # KI-Assistent
│   ├── main.py             # CLI Einstiegspunkt
│   └── *.docx/*.pptx/*.xlsx # Generierte Dokumente
│
└── SHARED_BRAIN/           # Gemeinsames Wissen
    ├── MEMORY.md           # Agent-Reports
    ├── SOLUTIONS.md        # Loesungsvorschlaege
    ├── BILLI_STATUS.md     # Billi-Status
    ├── RULES.md            # Verfassung
    └── *.md                # PM-Dokumentation
```

---

## Komponenten

### 1. Bridge (Watchdog)
Ueberwacht den Obsidian Vault und leitet Nachrichten weiter.

```bash
cd C:\Users\USass\Billi_Bilder\agent
python bridge.py
```

### 2. MCP Server
Verbindet Claude Desktop mit dem lokalen System.

```bash
python billi_mcp_server.py
```

### 3. Waechter (Stage 1)
Prueft Dateien und schreibt Reports.

```bash
python agent_loop.py
```

### 4. Denker (Stage 2)
Analysiert mit Ollama.

```bash
python denker.py
```

---

## Schnellstart

### Alles starten (empfohlen)
```bash
START_ALL.bat
```

### Einzelne Komponenten
```bash
# Bridge + MCP
START_BRIDGE.bat

# Waechter + Denker
python agent_loop.py
python denker.py
```

---

## Obsidian Vault

```
C:\claude\Udo-Vault\Topics\Agent-Bridge\
├── CLAUDE_TO_BILLI.md    # Claude schreibt hier
├── BILLI_TO_CLAUDE.md   # Billi antwortet hier
└── BRIDGE_LOG.md        # Log aller Nachrichten
```

---

## Claude Desktop Integration

1. Config bearbeiten:
   `C:\Users\USass\AppData\Roaming\Claude\claude_desktop_config.json`

2. Hinzufuegen:
```json
{
  "mcpServers": {
    "billi-bridge": {
      "command": "python",
      "args": ["C:\\Users\\USass\\Billi_Bilder\\agent\\billi_mcp_server.py"]
    }
  }
}
```

3. Claude Desktop neu starten

---

## Verfuegbare Befehle (nach MCP-Integration)

```
Was sagt Billi?
-> get_billi_thoughts()

Sag Billi X
-> send_to_billi("X")

Bridge Status?
-> get_bridge_status()
```

---

## Zertifikate (Udo Sassik)

1. Claude 101 (Anthropic)
2. Claude Code in Action (Anthropic)
3. Introduction to Claude Cowork (Anthropic)
4. AI Fluency: Framework & Foundations (Anthropic)
5. AI Fundamentals (IBM)
6. Project Management Fundamentals (IBM)

---

## Nächste Schritte

- [ ] Claude Desktop Config aktualisieren
- [ ] Stage 3 (Ausfuehrer) entwickeln
- [ ] Mehr Agenten-Funktionalitaet

---

*Erstellt: 07.04.2026*
*System: 100% lokal | 0 Euro | Ollama llama3.1*
