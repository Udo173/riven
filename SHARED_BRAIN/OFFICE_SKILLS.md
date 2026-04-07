# Word & Excel Skills - Installiert ✅

## Installierte Bibliotheken

| Format | Bibliothek | Installiert | Version |
|--------|------------|-------------|---------|
| Word (.docx) | python-docx | ✅ | 1.2.0 |
| Excel (.xlsx) | openpyxl | ✅ | 3.1.5 |
| Datenanalyse | pandas | ✅ | 3.0.2 |

---

## Word Dateien (.docx)

### Lesen
```python
from docx import Document

doc = Document("datei.docx")
for para in doc.paragraphs:
    print(para.text)

# Tabellen auslesen
for table in doc.tables:
    for row in table.rows:
        print([cell.text for cell in row.cells])
```

### Schreiben
```python
from docx import Document

doc = Document()
doc.add_heading("Titel", 0)
doc.add_paragraph("Text hier...")
doc.add_table(rows=2, cols=3)  # Tabelle hinzufügen
doc.save("neue_datei.docx")
```

---

## Excel Dateien (.xlsx)

### Lesen
```python
import openpyxl

wb = openpyxl.load_workbook("datei.xlsx")
sheet = wb.active

# Alle Zeilen
for row in sheet.iter_rows(values_only=True):
    print(row)

# Bestimmte Zelle
print(sheet["A1"].value)

# Nach Name
sheet = wb["Tabellenname"]
```

### Schreiben
```python
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Daten"

sheet["A1"] = "Name"
sheet["B1"] = "Wert"
sheet["A2"] = "Beispiel"
sheet["B2"] = 123

wb.save("neue_datei.xlsx")
```

---

## Datenanalyse mit Pandas

### Excel lesen
```python
import pandas as pd

df = pd.read_excel("datei.xlsx")
print(df.head())  # Erste Zeilen
print(df.columns)  # Spalten
print(df.describe())  # Statistik

# Filtern
df_filtered = df[df["Spalte"] > 100]

# Export
df_filtered.to_excel("output.xlsx")
```

### CSV
```python
df = pd.read_csv("datei.csv")
df.to_csv("output.csv")
```

---

## Nützliche Funktionen

### Word: Projekt-Charter aus Vorlage erstellen
```python
from docx import Document

def create_project_charter(name, description, budget):
    doc = Document()
    doc.add_heading("Project Charter", 0)
    
    doc.add_heading("Project Name", 1)
    doc.add_paragraph(name)
    
    doc.add_heading("Description", 1)
    doc.add_paragraph(description)
    
    doc.add_heading("Budget", 1)
    doc.add_paragraph(f"${budget:,}")
    
    doc.save(f"{name}_charter.docx")

create_project_charter("Mein Projekt", "Beschreibung", 50000)
```

### Excel: Projekt-Tracker erstellen
```python
import openpyxl

def create_project_tracker(tasks):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Tasks"
    
    # Header
    headers = ["Task", "Status", "Due Date", "Priority"]
    ws.append(headers)
    
    # Data
    for task in tasks:
        ws.append(task)
    
    wb.save("project_tracker.xlsx")
```

---

## Online Tools (Alternativen)

| Tool | URL | Kostenlos |
|------|-----|-----------|
| Google Docs | docs.google.com | ✅ |
| Office Online | office.com | ✅ |
| LibreOffice | libreoffice.org | ✅ |

---

## Praxis-Beispiel: Project Charter aus Excel erstellen

```python
import openpyxl
from docx import Document

# Excel lesen
wb = openpyxl.load_workbook("project_data.xlsx")
sheet = wb.active

# Word erstellen
doc = Document()
doc.add_heading("Project Charter", 0)

# Daten übertragen
for row in sheet.iter_rows(values_only=True):
    if row[0]:
        doc.add_paragraph(f"{row[0]}: {row[1]}")

doc.save("Project_Charter.docx")
print("Charter erstellt!")
```

---

**Stand:** 06.04.2026
**Status:** Installiert und einsatzbereit ✅
