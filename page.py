from PyPDF2 import PdfReader, PdfWriter

# Input files
pdf1 = PdfReader("pdf1.pdf")
pdf2 = PdfReader("pdf2.pdf")

# Output writer
writer = PdfWriter()

# Add pages 1–5 from pdf1 (Python uses 0-based index, so 0–4)
for i in range(0, 5):
    writer.add_page(pdf1.pages[i])

# Add pages 6–20 from pdf2 (so indices 5–19)
for i in range(5, 20):
    writer.add_page(pdf2.pages[i])

# Write to merged file
with open("merged.pdf", "wb") as f:
    writer.write(f)
