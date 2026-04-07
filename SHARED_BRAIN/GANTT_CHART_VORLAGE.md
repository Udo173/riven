# GANTT CHART - Vorlage mit Duration-Berechnung

## Definition:
> **Duration** = Zeit die ein Task braucht = End-Datum - Start-Datum + 1

---

## Basis Vorlage:

```
┌────────────────────────────────────────────────────────────────────┐
│                        TASK LIST                                    │
├──────────────┬──────────┬──────────┬────────────┬────────────────┤
│ Task        │ Start    │ Ende     │ Duration   │ Status         │
├──────────────┼──────────┼──────────┼────────────┼────────────────┤
│              │ TT.MM.JJ │ TT.MM.JJ │ ? Tage     │                │
│              │          │          │            │                │
│              │          │          │            │                │
│              │          │          │            │                │
│              │          │          │            │                │
│              │          │          │            │                │
└──────────────┴──────────┴──────────┴────────────┴────────────────┘
```

---

## Mit Beispiel ausgefüllt:

```
┌────────────────────────────────────────────────────────────────────┐
│                        TASK LIST                                    │
├──────────────┬──────────┬──────────┬────────────┬────────────────┤
│ Task         │ Start    │ Ende     │ Duration   │ Status         │
├──────────────┼──────────┼──────────┼────────────┼────────────────┤
│ 2.2 Wirefr. │ 01.04.26 │ 08.04.26 │ 7.5 Tage  │ 🔄 Active      │
├──────────────┼──────────┼──────────┼────────────┼────────────────┤
│ 3.1 Invoicing│ 09.04.26 │ 11.04.26 │ 3 Tage    │ ⏳ Pending     │
├──────────────┼──────────┼──────────┼────────────┼────────────────┤
│              │          │          │            │                │
└──────────────┴──────────┴──────────┴────────────┴────────────────┘
```

---

## Excel Vorlage:

| A | B | C | D | E |
|---|---|---|---|---|
| **Task** | **Start** | **Ende** | **Duration** | **Status** |
| Task 1 | 01.04.2026 | 08.04.2026 | =C2-B2+1 | Done |
| Task 2 | 09.04.2026 | 11.04.2026 | =C3-B3+1 | Pending |

---

## Gantt Chart Diagramm:

```
TASK           | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
───────────────┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───+
2.2 Wireframes|███│███│███│███│███│███│███│██░│   │   │
───────────────┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───+
3.1 Invoicing │   │   │   │   │   │   │   │   │███│███│
───────────────┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───+
              |   |   |   |   |   |   |   |   |   |   │
              
███ = Arbeitstage
░░░ = Halber Tag
```

---

## Formel Quick Reference:

```
Duration = Ende - Start + 1

Beispiel:
Start: 01.04.2026
Ende:   08.04.2026
─────────────────
Duration: 8 - 1 + 1 = 8 Tage
```

---

## Checkliste:

- [ ] Alle Tasks aufgelistet
- [ ] Start-Datum gesetzt
- [ ] Ende-Datum gesetzt
- [ ] Duration berechnet
- [ ] Status aktuell
- [ ] Gantt Chart erstellt

---

**Erstellt:** 06.04.2026
**Quelle:** Project Management Kurs
