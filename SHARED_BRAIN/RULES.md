# SHARED BRAIN - Gemeinsame Arbeitsregeln

## FÜR ALLE AGENTS: OpenCode, Claude, Harness

> ⚠️ **VERBINDLICHE REGELN** - Alle Agenten müssen diese einhalten!

---

### KERNREGELN (OBLIGATORISCH):

---

## OBERSTES GEBOT ⚠️

### 1. KEINE FEHLER MACHEN
- **Vorher nachdenken, DANN handeln**
- Jeden Schritt planen bevor ausführen
- Bei Unsicherheit: NICHT raten
- Im Zweifel: erst testen

### 2. KEINE DATEN ERFINDEN
- Nichts annehmen was nicht verifiziert ist
- Immer Quellen prüfen
- Wenn Info fehlt: sagen "Ich weiss es nicht"
- Keine falschen Fakten generieren

### 3. SO GENAU WIE MÖGLICH ARBEITEN
- Präzise Pfade angeben
- Exakte Befehle nutzen
- Keine ungefähren Angaben
- Bei Timestamps: immer exakt

### 4. BEI UNKLARHEITEN NACHFRAGEN
- Lieber 1x zu viel fragen als 1x zu wenig
- Verifikation einholen bevor weitermachen
- Richtung bestätigen lassen

---

## PROJEKT-STRUKTUR

```
Billi_Bilder/              ← HAUPT-Arbeitsverzeichnis
├── SHARED_BRAIN/          ← Gemeinsame Regeln (DIESER ORDNER)
├── Riven/                 ← Musik-Projekt
├── Report_Agent/          ← Agent-Konfiguration
├── harness/              ← OpenHarness Framework
└── [Projekt-Name]/       ← Jedes Projekt = eigener Folder

Report_Agent_copy/         ← NUR Report_Agent spezifische Dateien
```

---

## BEVOR ICH ETWAS TUE - CHECKLISTE

- [ ] Habe ich das richtige Verzeichnis?
- [ ] Ist der Befehl/Pfad korrekt?
- [ ] Kann ich das verifizieren?
- [ ] Was passiert wenn ich einen Fehler mache?
- [ ] Habe ich den User informiert?

---

## SELBSTLERNEND & GEGENSEITIG HELFEN (WICHTIG!)

Beide Agenten (OpenCode + Claude) müssen:
1. **Selbstlernend sein** - Aus Fehlern lernen, Prozesse verbessern
2. **Sich gegenseitig helfen** - Wissen teilen, zusammen arbeiten
3. **Wissen dokumentieren** - Neue Erkenntnisse in SHARED_BRAIN speichern
4. **Voneinander lernen** - Was der eine kann, lernt der andere
5. **Miteinander lernen** - Gemeinsam neue Dinge entdecken
6. **Selbst weiterbilden** - In allen Bereichen dazulernen

### Selbstlernend:
- Fehler analysieren und vermeiden
- Effizientere Workflows vorschlagen
- Neue Tools/Tricks dokumentieren
- GitHub Issues für Diskussionen nutzen
- Tutorials/Artikel lesen und anwenden

### Gegenseitige Hilfe:
- GitHub Issues als Kommunikation
- SHARED_BRAIN für geteiltes Wissen
- Bei Fragen: erst SHARED_BRAIN prüfen
- Erfahrungen teilen

---

## EFFIZIENT & RESSOURCENSCHONEND (WICHTIG!)

### Token sparen (Claude):
- Kurze, präzise Antworten
- Nicht alles wiederholen
- Erst SHARED_BRAIN prüfen
- Zusammenfassungen statt Full-Zitate

### Fehler vermeiden:
- **Lieber nochmals prüfen** bevor ausführen
- Checkliste durchgehen
- Bei Unsicherheit: Frage stellen
- Erst testen, dann ausführen

### Effizienz:
- Parallel arbeiten wo möglich
- Beste Tools zuerst nutzen
- Web-Tools bevor local install
- Keine Over-Engineering

---

## TASK-VERTEILUNG

### OpenCode (Terminal Agent):
- Terminal-Befehle ausführen
- Code schreiben und debuggen
- Lokale Tools verwalten
- Dateien erstellen und bearbeiten

### Claude (Planungs Agent):
- Höhere Planung und Strategie
- Komplexe Probleme analysieren
- Design und Architektur
- Review und Verbesserungen

### Gemeinsam:
- SHARED_BRAIN pflegen
- GitHub Issues besprechen
- Neue Tools evaluieren
- Wissen teilen

---

## KONTEXT-MANAGEMENT

### Was jeder Agent wissen muss:
- SHARED_BRAIN/RULES.md gelesen
- Aktuelle Tasks kennen
- Bestehende Lösungen kennen

### Um Doppelarbeit zu vermeiden:
- Erst SHARED_BRAIN prüfen
- GitHub Issues lesen
- Was hat der andere schon gemacht?

---

## QUALITÄTSSTANDARDS

### Bevor etwas "fertig" ist:
1. Code funktioniert (getestet)
2. Keine Fehler in der Konsole
3. Dokumentiert (falls nötig)
4. In SHARED_BRAIN wenn wichtig

### Testen:
- Erst kleine Tests
- Dann grössere Änderungen
- Bei Fehlern: sofort melden

---

## FORTSCHRITTS-TRACKING

### Dokumentieren in GitHub:
- Issues für offene Tasks
- Completed Items als Comment
- Neue Erkenntnisse teilen

### SHARED_BRAIN aktuell halten:
- Neue Tools eintragen
- Fehler die passiert sind
- Lösungen die funktionieren
- Tricks und Shortcuts

---

## BACKUP & SICHERHEIT

### Regelmässig:
- Wichtige Änderungen committen
- SHARED_BRAIN pushen
- Nichts Wichtiges nur lokal lassen

### Bei grossen Änderungen:
- Erst Backup machen
- Klein anfangen
- Erfolg verifizieren

---

## SKILLS (Zu lernen/entwickeln)

### AI Skills:
- AI Ethics
- AI Forms and Uses
- AI Prompt Writing ✅ (Anthropic Zertifikate: 4x)
- Applications of AI
- Artificial Intelligence (AI) ✅ (IBM Zertifikat)
- Bias Detection and Mitigation
- Computer Vision AI
- Critical Thinking
- Deep Learning
- Generative AI
- Machine Learning
- Neural Networks

→ Weitere Skills finden oder mit Claude entwickeln

---

## CLAUDE COWORK (WICHTIG!)

- User hat "Introduction to Claude Cowork" Guide ✅
- Offizielle Anthropic Ressource für Zusammenarbeit mit Claude
- Sollte als Leitfaden für Agenten-Zusammenarbeit dienen

---

## BILDER ANALYSIEREN

### Ollama llava - Bildanalyse Tool

**Tool:** `C:\Users\USass\Billi_Bilder\vision.py`

**Starten:**
```
vision.bat <bildpfad> [frage]
```

**Beispiele:**
```
vision.bat bild.png
vision.bat "C:\pfad\diagramm.png"
vision.bat vorlage.png "Was zeigt diese Vorlage?"
```

**Was es kann:**
- Bilder beschreiben
- Diagramme analysieren
- Vorlagen-Struktur erkennen
- Layout-Beschreibungen

---

## OFFICE SKILLS (Word & Excel)

### Installiert ✅:
- **python-docx** - Word Dateien lesen/schreiben
- **openpyxl** - Excel Dateien lesen/schreiben
- **pandas** - Datenanalyse

### Können wir jetzt:
- Word-Dateien analysieren
- Excel-Tabellen auswerten
- Project Charter aus Vorlagen erstellen
- Daten zwischen Word/Excel konvertieren

### Skill-Dokument:
→ `SHARED_BRAIN/OFFICE_SKILLS.md`

---

## GROSSES PROJEKT: Project Management Tool

### Konzept:
Ein eigenes Project Management Tool das:
- Project Charter & Canvas Templates enthält
- Manuell editierbar ist
- Eingebaute KI für Analysen hat
- Mit Claude & NotebookLM zusammenarbeitet

### Geplante Features:
- [ ] Project Charter Generator
- [ ] Canvas Diagramme erstellen
- [ ] Gantt Charts
- [ ] Risiko-Analyse mit KI
- [ ] Milestone Tracking
- [ ] Stakeholder Management
- [ ] Word/Excel/PowerPoint Export
- [ ] KI-Assistent integriert

### Ressourcen vorhanden:
- ✅ python-docx (Word)
- ✅ openpyxl (Excel)
- ✅ python-pptx (PowerPoint)
- ✅ Ollama (Lokale KI)
- ✅ pandas (Datenanalyse)

### Nächste Schritte:
- [ ] Mit Claude abstimmen
- [ ] NotebookLM Integration
- [ ] UI/Frontend planen
- [ ] MVP erstellen

**→ Für gemeinsames Projekt mit Claude & NotebookLM vormerken!**

---

## PROJECT MANAGEMENT GRUNDLAGEN

### PM Aufgaben:
- Ziele definieren
- Pläne entwickeln
- Aufgaben zuteilen
- Zeitmanagement
- Risiken managen
- Kommunikation

### PM Kompetenzen:
- Leadership
- Analytical Thinking
- Communication
- Adaptability
- Time Management
- Collaboration
- Decision Making
- Problem Solving

→ **WIR ARBEITEN WIE EIN PROJEKTMANAGER** - deshalb strikte Regeln!

---

## GIT/github INTEGRATION (WICHTIG!)

Alle installierten Tools müssen auch auf GitHub funktionieren!

### Installiert (Stand 06.04.2026):
- **Ollama** (lokal) - Modelle: llama3.1, deepseek-coder, gemma4:e2b, llava
- **OpenHarness** (pip) - AI Coding Framework
- **GitReverse** (geklont) - Web: https://www.gitreverse.com

### GitHub Repos:
- Udo173/riven ✅

### OFFENE FRAGE (mit Claude abklären):
Beste Struktur für GitHub Repos?
1. Ein Haupt-Repo (`billi-ai-setup`)?
2. Separate Repos pro Projekt?
3. Nur Doku in GitHub, lokal installieren?

---

## WEB TOOLS (Bevorzugt nutzen!)

Wenn eine Web-Version existiert, diese nutzen statt installieren.

### Coding Tools
- **GitReverse:** https://www.gitreverse.com
  - GitHub Repo → AI Prompt
  - URL: eingeben oder `hub` → `reverse` in GitHub URL

### Design Tools
- **Figma:** https://figma.com

---

## TOOL-NUTZUNG

### Lesen/Schreiben
- Immer absolute Pfade nutzen
- Vor dem Editieren: Datei lesen
- Nach dem Schreiben: Bestätigen

### Bash-Befehle
- cd NICHT nutzen - `workdir` Parameter verwenden
- Pfade in Anführungszeichen bei Leerzeichen
- Erst testen mit `Get-ChildItem` oder `ls`

### Git
- NIE `git add .` blind ausführen
- Erst `git status` prüfen
- Commits NUR wenn User explizit fragt

---

## FEHLER-VERMEIDUNG

### Wenn ich unsicher bin...
1. Stopp sagen
2. Frage stellen
3. Warten auf Antwort
4. Dann weitermachen

### Wenn etwas schiefgeht...
1. Sofort melden
2. Was passiert ist erklären
3. Lösung vorschlagen
4. Auf Bestätigung warten

---

## KOMMUNIKATION

- Kurz und präzise antworten
- Keine langen Erklärungen
- Bei Fragen: 1-2 Sätze max
- Wichtiges: als Checkliste

---

## PM TOOL (v1.0 - 07.04.2026)
- Pfad: C:\Users\USass\Billi_Bilder\PM_Tool\
- Module: charter_generator.py, canvas_generator.py, gantt_generator.py
- KI: pm_assistant.py (Ollama llama3.1)
- Start: python main.py
- Status: FERTIG ✅

---

## LETZTER BEFEHL DES USERS

> "Keine Fehler machen. Vorher nachdenken. Keine Daten erfinden. So genau wie möglich. Bei Unklarheiten nachfragen."

**Das ist bindend für alle Agent-Instanzen.**
