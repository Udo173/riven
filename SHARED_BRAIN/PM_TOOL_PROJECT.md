# PROJECT MANAGEMENT TOOL - Projektplan

## Vision

Ein eigenes Project Management Tool das:
- Professionelle Project Charter & Canvas Templates bietet
- Manuell editierbar bleibt
- Eingebaute KI für Analysen und Vorschläge nutzt
- Mit Claude & NotebookLM zusammenarbeitet

---

## Projektname (offen)

Mögliche Namen:
- **ProjectForge** - Projekte schmieden
- **CanvasPro** - Canvas-basiertes PM
- **PMStudio** - Project Management Studio
- **CharterAI** - Charter mit KI

---

## Kernfeatures

### 1. Dokumenten-Generation
| Feature | Beschreibung | Format |
|---------|-------------|--------|
| Project Charter | Professionelles Charter erstellen | Word, PDF |
| Project Canvas | Visuelles Canvas (9-Felder) | PowerPoint, PNG |
| Gantt Chart | Zeitlinien-Darstellung | Excel, PNG |
| Status Reports | Automatische Reports | Word, PDF |

### 2. KI-Funktionen (eingebaut)
| Feature | Beschreibung |
|---------|-------------|
| Risiko-Analyse | KI analysiert Risiken & Vorschläge |
| Ziel-Optimierung | KI schlägt messbare KPIs vor |
| Text-Generierung | KI hilft beim Schreiben |
| Zusammenfassung | KI fasst Dokumente zusammen |
| Übersetzung | Multi-language Support |

### 3. Zusammenarbeit
| Tool | Integration |
|------|-------------|
| Claude | Per API / GitHub Issues |
| NotebookLM | Recherche & Zusammenfassung |
| OpenCode | Dokumenten-Generierung |
| GitHub | Versionierung & Backup |

---

## Technischer Stack

### Backend
- Python 3.10+
- pandas (Datenanalyse)
- openpyxl (Excel)
- python-docx (Word)
- python-pptx (PowerPoint)

### KI (Lokal)
- Ollama
- Modelle: llama3.1, gemma4, etc.
- Alternativ: Claude API, OpenAI API

### Frontend (offen)
- Option A: Web-App (Streamlit, Gradio)
- Option B: Desktop (PyQt, Tkinter)
- Option C: Web + Desktop hybrid

### Export
- Word (.docx)
- Excel (.xlsx)
- PowerPoint (.pptx)
- PDF
- PNG/JPG Diagramme

---

## Benutzerflow

```
1. START
   ↓
2. NEUES PROJEKT oder VORLAGE WÄHLEN
   ↓
3. PROJECT CHARTER AUSFÜLLEN
   - Name, Beschreibung, Zweck
   - Goals, Scope, Deliverables
   - Stakeholder, Budget
   ↓
4. PROJECT CANVAS ERSTELLEN
   - 9-Felder ausfüllen
   - Manuell oder mit KI-Hilfe
   ↓
5. KI-ANALYSE (optional)
   - Risiken bewerten
   - Vorschläge einholen
   ↓
6. GANTT CHART GENERIEREN
   - Meilensteine setzen
   - Timeline erstellen
   ↓
7. EXPORT
   - Word, Excel, PowerPoint, PDF
   ↓
8. REVIEW & TEILEN
   - Claude/NotebookLM Integration
   - GitHub Backup
```

---

## Milestones (Vorschlag)

| Phase | Datum | Ziel |
|-------|-------|------|
| Planning | Week 1-2 | Konzept finalisieren, Tech-Stack wählen |
| MVP | Week 3-4 | Basic Charter & Canvas Generator |
| KI Integration | Week 5-6 | Ollama/Claude Integration |
| UI/UX | Week 7-8 | Frontend entwickeln |
| Export | Week 9-10 | Word/Excel/PowerPoint Export |
| Test | Week 11-12 | Testen & Bugfixes |
| Release | Week 13 | Erste Version release |

---

## Checkliste

- [ ] Projektname wählen
- [ ] Tech-Stack finalisieren
- [ ] MVP planen
- [ ] Mit Claude abstimmen
- [ ] NotebookLM Integration planen
- [ ] UI/UX Design starten

---

**Erstellt:** 06.04.2026
**Status:** Planning
**Beteiligte:** User, OpenCode, Claude
