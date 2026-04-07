# PROJECT TRACKER - Excel Diagramm Beispiel

## Beispiel: Aufgaben-Übersicht

```
┌─────────────────────────────────────────────────────────────┐
│                    PROJECT TRACKER                          │
│                  Riven Musik-Projekt                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  TASK              │ STATUS    │ DUE      │ PRIORITY      │
│  ─────────────────┼───────────┼──────────┼─────────────  │
│  Motion Graphics  │ ✅ Done    │ 05.04.26 │ 🔴 High       │
│  Cover Design     │ ✅ Done    │ 06.04.26 │ 🔴 High       │
│  Lyric Video     │ 🔄 Active  │ 15.04.26 │ 🔴 High       │
│  AI Video        │ ⏳ Pending │ 01.05.26 │ 🟡 Medium     │
│  Final Compile   │ ⏳ Pending │ 15.05.26 │ 🟡 Medium     │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  STATUS ÜBERSICHT                                          │
│                                                             │
│  ✅ Done (2)      ████████████░░░░░░░░  40%             │
│  🔄 Active (1)    ██████░░░░░░░░░░░░░░  20%             │
│  ⏳ Pending (2)   ████████████░░░░░░░░  40%             │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PRIORITY VERTEILUNG                                       │
│                                                             │
│  🔴 High (2)    ████████████████░░░░  60%               │
│  🟡 Medium (2)   ████████████████░░░░  60%               │
│  🟢 Low (0)      ░░░░░░░░░░░░░░░░░░░░  0%               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Gantt Chart Beispiel

```
GANTT CHART - Riven Projekt
═══════════════════════════════════════════════════════════════

KW        │ 14 │ 15 │ 16 │ 17 │ 18 │ 19 │ 20 │ 21 │
──────────┼────┼────┼────┼────┼────┼────┼────┼────┤
          │    │    │    │    │    │    │    │    │
Motion    │████│████│    │    │    │    │    │    │
Graphics  │    │    │    │    │    │    │    │    │
──────────┼────┼────┼────┼────┼────┼────┼────┼────┤
          │    │    │    │    │    │    │    │    │
Cover     │    │████│████│    │    │    │    │    │
Design    │    │    │    │    │    │    │    │    │
──────────┼────┼────┼────┼────┼────┼────┼────┼────┤
          │    │    │    │    │    │    │    │    │
Lyric     │    │    │████│████│████│    │    │    │
Video     │    │    │    │    │    │    │    │    │
──────────┼────┼────┼────┼────┼────┼────┼────┼────┤
          │    │    │    │    │    │    │    │    │
AI        │    │    │    │    │████│████│████│    │
Video     │    │    │    │    │    │    │    │    │
──────────┼────┼────┼────┼────┼────┼────┼────┼────┤
          │    │    │    │    │    │    │    │    │
Final     │    │    │    │    │    │    │████│████│
Compile   │    │    │    │    │    │    │    │    │
          │    │    │    │    │    │    │    │    │
═══════════════════════════════════════════════════════════════
```

---

## Excel Daten-Struktur

| A | B | C | D | E |
|---|---|---|---|---|
| **Task** | **Status** | **Start** | **Ende** | **Fortschritt** |
| Motion Graphics | Done | 01.04.26 | 05.04.26 | 100% |
| Cover Design | Done | 04.04.26 | 06.04.26 | 100% |
| Lyric Video | Active | 07.04.26 | 15.04.26 | 30% |
| AI Video | Pending | 16.04.26 | 01.05.26 | 0% |
| Final Compile | Pending | 02.05.26 | 15.05.26 | 0% |

---

## So erstellst du es:

### In Excel:
1. Öffne Excel
2. Trage Daten in Spalten ein
3. Markiere Daten
4. Einfügen → Diagramme → Bar/Column/Gantt

### Mit Python:
```python
import openpyxl
from openpyxl.chart import BarChart, Reference

wb = openpyxl.Workbook()
ws = wb.active

# Header
headers = ["Task", "Fortschritt %", "Status"]
for col, header in enumerate(headers, 1):
    ws.cell(row=1, column=col, value=header)

# Data
data = [
    ["Motion Graphics", 100, "Done"],
    ["Cover Design", 100, "Done"],
    ["Lyric Video", 30, "Active"],
    ["AI Video", 0, "Pending"],
    ["Final Compile", 0, "Pending"],
]

for row_idx, row_data in enumerate(data, 2):
    for col_idx, value in enumerate(row_data, 1):
        ws.cell(row=row_idx, column=col_idx, value=value)

# Chart erstellen
chart = BarChart()
chart.type = "col"
chart.title = "Projekt Fortschritt"
data = Reference(ws, min_col=2, min_row=1, max_row=6)
chart.add_data(data)

ws.add_chart(chart, "E2")
wb.save("project_tracker.xlsx")
```

---

**Erstellt:** 06.04.2026
