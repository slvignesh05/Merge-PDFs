# 📄 PDF Merger Script

A simple Python script to automatically merge all PDF files in a folder into a single PDF.  
Useful for combining mark sheets, reports, or any multi-file PDF collection.

---

## 🚀 Features
- Automatically detects all `.pdf` files in a folder
- Merges them into one PDF
- Sorts files alphabetically for predictable order
- Lightweight, no GUI, quick execution

---

## 📂 How to Use

### 1️⃣ Install Python
Make sure you have Python 3 installed.  
Check with:
```
python --version
```

### Install Dependencies

The script uses PyPDF2:

`pip install PyPDF2`

### Add Your PDF Files

Place all your PDF files in the same folder as the script.

### Run the Script
`python merge_pdfs.py`

📜 What the Script Does

Detects all PDF files in the folder

Sorts them alphabetically

Merges them into merged_all_pdfs.pdf
