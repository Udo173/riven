# PM TOOL - UI KONZEPTE
## Lern-Vorlagen fuer Design mit ChatGPT/Gemini

---

## KONZEPT 1: Dashboard (Hauptseite)

```
┌─────────────────────────────────────────────────────────┐
│  [Logo]  PM TOOL                    [User] [Settings]   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐   │
│  │   PROJEKTE   │ │  CHARTER     │ │   GANTT      │   │
│  │   [12]       │ │   [5]        │ │   [8]        │   │
│  │   [+ Neu]     │ │   [+ Neu]     │ │   [+ Neu]     │   │
│  └──────────────┘ └──────────────┘ └──────────────┘   │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │  AKTIVE PROJEKTE                               │   │
│  │  ───────────────────────────────────────────   │   │
│  │  ● PM Tool           ████████░░ 80%   [Edit]   │   │
│  │  ● Riven Video       ████░░░░░░░ 40%   [Edit]   │   │
│  │  ● SGS Auftrag       ██████████░░ 90%   [Edit]   │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  ┌──────────────┐ ┌──────────────┐                     │
│  │ NAECHSTE     │ │ QUICK        │                     │
│  │ MEILENSTEINE │ │ ACTIONS      │                     │
│  │ ──────────── │ │ ──────────── │                     │
│  │ 15.04 PM Tool│ │ [Charter]   │                     │
│  │ 20.04 Review │ │ [Canvas]    │                     │
│  │ 30.04 Release│ │ [Gantt]     │                     │
│  └──────────────┘ └──────────────┘                     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Farben:**
- Header: Dunkelblau (#1F497D)
- Akzent: Gold (#FFD166)
- Cards: Hellblau (#F0F4F9)
- Text: Dunkelgrau (#1A1A1A)

---

## KONZEPT 2: Project Charter Editor

```
┌─────────────────────────────────────────────────────────┐
│  ← Zurueck    PROJECT CHARTER BEARBEITEN    [Speichern]│
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────────────┐  ┌─────────────────────────┐ │
│  │ PROJEKT-INFORMATIONEN│  │ STAKEHOLDER             │ │
│  │ ───────────────────│  │ ──────────────────────│ │
│  │ Name: [___________] │  │ ┌─────────────────────┐│ │
│  │ Leiter: [_________] │  │ │ Name  | Rolle | Int││ │
│  │ Sponsor: [_________] │  │ ├─────────────────────┤│ │
│  │ Start: [___] [Kal]  │  │ │ Udo    | PM    | ●●●││ │
│  │ Ende:  [___] [Kal] │  │ │ Claude | Arch  | ●● ││ │
│  │ Status: [Dropdown] │  │ │ Billi  | Exec  | ●● ││ │
│  └─────────────────────┘  │ └─────────────────────┘│ │
│                           │ [+ Stakeholder hinzufuegen]│ │
│  ┌─────────────────────┐  └─────────────────────────┘ │
│  │ PROJEKTZIEL        │                                │
│  │ ───────────────────│                                │
│  │ ┌─────────────────┐│                                │
│  │ │                 ││                                │
│  │ │ Textarea        ││                                │
│  │ │                 ││                                │
│  │ └─────────────────┘│                                │
│  └─────────────────────┘                                │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │ MEILENSTEINE                                    │   │
│  │ [+ Meilenstein]                                  │   │
│  │ ┌──────────────────────────────────────────┐   │   │
│  │ │ M1 | Design fertig | 15.04 | [Status]   │   │   │
│  │ │ M2 | Review | 20.04 | [Status]           │   │   │
│  │ └──────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## KONZEPT 3: Gantt Chart View

```
┌─────────────────────────────────────────────────────────┐
│  GANTT CHART                        [Export] [Filter] │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Projekt: [Dropdown ▼]        Zeitraum: [Apr ▼] 2026  │
│                                                         │
│  Mo Di Mi Do Fr Sa So Mo Di Mi Do Fr Sa So Mo Di ... │
│  ────────────────────────────────────────────────────  │
│  Aufgabe 1          ████████                          │
│  Aufgabe 2                    ██████████              │
│  Aufgabe 3        ██████                              │
│  Aufgabe 4                      ████                   │
│  Meilenstein 1                    ◆                   │
│  Aufgabe 5                              ████████████   │
│                                                         │
│  ────────────────────────────────────────────────────  │
│  ■ In Arbeit  ██ Fertig  ◆ Meilenstein  ░ Wochenende │
│                                                         │
│  LEGENDE:                                              │
│  [█] [█] [█] [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]│
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## KONZEPT 4: Dark Mode Dashboard

```
┌─────────────────────────────────────────────────────────┐
│  ◐ PM TOOL                      🔔 [User] ⚙️ 🌓        │
├─────────────────────────────────────────────────────────┤
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
│                                                         │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐       │
│  │ ▓▓▓▓▓▓▓▓▓ │  │ ▓▓▓▓▓▓▓▓▓ │  │ ▓▓▓▓▓▓▓▓▓ │       │
│  │  PROJEKTE  │  │  AKTIV     │  │  FERTIG    │       │
│  │     12     │  │     3      │  │     9      │       │
│  │ ░░░░░░░░░░ │  │ ████░░░░░░ │  │ ██████████░ │       │
│  └────────────┘  └────────────┘  └────────────┘       │
│                                                         │
│  ┌─────────────────────────────────────────────────┐  │
│  │  RECENT ACTIVITY                                │  │
│  │  ────────────────────────────────────────────   │  │
│  │  🟢 PM Tool Charter aktualisiert - vor 2h       │  │
│  │  🟡 Gantt Chart erstellt - vor 5h               │  │
│  │  🟢 Canvas exportiert - vor 1d                 │  │
│  └─────────────────────────────────────────────────┘  │
│                                                         │
└─────────────────────────────────────────────────────────┘

Farben (Dark):
- Background: #0D1117
- Cards: #161B22
- Text: #E6EDF3
- Akzent: #58A6FF
- Success: #3FB950
- Warning: #D29922
```

---

## KONZEPT 5: Mobile Responsive

```
┌─────────────────┐
│ ☰  PM TOOL   👤 │
├─────────────────┤
│                 │
│  ┌───────────┐  │
│  │  PROJEKTE │  │
│  │    12     │  │
│  └───────────┘  │
│                 │
│  ┌───────────┐  │
│  │  AKTIV    │  │
│  │    3      │  │
│  └───────────┘  │
│                 │
│  ┌───────────┐  │
│  │  FERTIG   │  │
│  │    9      │  │
│  └───────────┘  │
│                 │
│  ──────────────  │
│                 │
│  🟢 PM Tool     │
│  ████████░░ 80% │
│                 │
│  🟡 Riven       │
│  ████░░░░░░ 40% │
│                 │
│  ──────────────  │
│                 │
│  [📊 Charter]   │
│  [📈 Canvas]    │
│  [📅 Gantt]     │
│                 │
└─────────────────┘
```

---

## Design-Prompts fuer ChatGPT/Gemini

### Prompt 1: Dashboard
```
Erstelle ein modernes Dashboard-Design fuer ein PM Tool.

Style: Clean, professionell, Corporate
Farben: Dunkelblau (#1F497D), Gold (#FFD166), Hellblau (#F0F4F9)
Elemente: Projekt-Karten, Status-Balken, Quick-Actions
```

### Prompt 2: Dark Mode
```
Erstelle ein Dark Mode Dashboard mit:
- Background: #0D1117
- Cards: #161B22
- Akzent: #58A6FF
- Neon-Glow Effekte
- Moderne, Tech-lastige Optik
```

---

*Vorlagen fuer ChatGPT/Gemini Design-Generierung*
