import os
from PyPDF2 import PdfMerger

# Folder containing the PDFs (use '.' for current folder)
folder_path = '.'

# Get all PDF files in the folder
pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]

# Sort alphabetically (so order is predictable)
pdf_files.sort()

print("Found PDFs in folder:")
for pdf in pdf_files:
    print(f" - {pdf}")

# Merge them
merger = PdfMerger()
for pdf in pdf_files:
    merger.append(os.path.join(folder_path, pdf))

output_file = "merged_all_pdfs.pdf"
merger.write(output_file)
merger.close()

print(f"\n✅ Merged PDF saved as {output_file}")
