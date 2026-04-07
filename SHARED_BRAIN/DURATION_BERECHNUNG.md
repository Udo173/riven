# TASK DURATION - Berechnung

## Definition:
> Duration (Dauer) ist die Zeit die ein Task braucht, basierend auf Start- und Enddatum.

## Formel:
```
Duration = End-Datum - Start-Datum + 1
```

*(+1 weil both Start und Ende zählen)*

---

## Beispiel aus dem Kurs:

### Task 2.2: Create wireframes and prototypes
```
Start: Tag X
Ende: Tag Y

Rechnung:
Duration = Ende - Start + 1
Duration = Y - X + 1

Ergebnis: 7,5 Tage
```

### Task 3.1: Develop invoicing module
```
Start: Tag A
Ende: Tag B

Ergebnis: 3 Tage
```

---

## Duration vs Effort

| Begriff | Bedeutung |
|---------|-----------|
| **Duration** | Kalendertage (inkl. Wochenenden) |
| **Effort** | Tatsächliche Arbeitsstunden |

---

## Excel-Formel:
```excel
=Enddatum - Startdatum + 1
```

---

## Für Gantt Chart:

```
Task          | Start | Ende | Duration |
--------------|-------|------|----------|
Wireframes    | Tag 1 | Tag 7.5 | 7.5 Tage |
Invoicing     | Tag 8 | Tag 10 | 3 Tage |
```

---

**Erstellt:** 06.04.2026
**Quelle:** Project Management Kurs
