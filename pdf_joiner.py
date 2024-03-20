# Requirments:
# - All pages should be merged alternatively starting from pdf1
# - All the pages of pdf2 should be taken starting from the latest
# - All pages of pdf1 should be taken starting from the first
# - Print the number of pages of pdf1, pdf2, and the sum of the pages
# - If the total pages number is odd, add a blank page
# - After pdf1 is finished, add all the reamaining pages of pdf2
# - If pdf2 has lessa pages than pdf1, add the remaining pages of pdf1
# - Print a warning message if the pages of pdf1 are less than pdf2
# - Get pdf1, pdf2, output as command line parameters
# - Use pypdf library

# Usage example: python pdf_joiner.py --pdf1 pdf1.pdf --pdf2 pdf2.pdf --output output.pdf

import argparse
from os import path
from pypdf import PdfReader, PdfWriter

parser = argparse.ArgumentParser(description = 'Merges 2 PDFs. First contains odd pages, second contains even pages but from latest to the first',)
parser.add_argument("--pdf1", required=True, help="path of the first PDF to merge")
parser.add_argument("--pdf2", required=True, help="path of the second PDF to merge")
parser.add_argument("--output", required=True, help="path of the output PDF")
args = parser.parse_args()

print(f"PDF 1: {args.pdf1}", end="")
if (not path.exists(args.pdf1)):
    print(f" {args.pdf1} does not exists.")
    exit()

pdf1 = PdfReader(args.pdf1)
num_pages_pdf1 = len(pdf1.pages)
print(f" has {num_pages_pdf1} pages.")

print(f"PDF 2: {args.pdf2}", end="")
if (not path.exists(args.pdf2)):
    print(f" {args.pdf2} does not exists.")
    exit()

pdf2 = PdfReader(args.pdf2)
num_pages_pdf2 = len(pdf2.pages)
print(f" has {num_pages_pdf2} pages.")

total_pages = num_pages_pdf1 + num_pages_pdf2
print(f"{args.output} PDF will have {total_pages} pages.")

output_pdf = PdfWriter()

# Merge the pages alternatively starting from pdf1
for i in range(num_pages_pdf1):
  output_pdf.add_page(pdf1.pages[i])

  # If there are still pages available in pdf2, add the i-th page from pdf2 starting from the last
  if i < num_pages_pdf2:
    output_pdf.add_page(pdf2.pages[num_pages_pdf2 - 1 - i])
  # Otherwise, if the pages of pdf2 are finished but there are still pages in pdf1, add a white page
  else:
    white_page = PdfReader.pdf.PageObject.createBlankPage() # Blank page
    output_pdf.add_page(white_page)

# If there are still pages in pdf2 that have not been merged, add them to the new PDF
if num_pages_pdf2 > num_pages_pdf1:
  for i in range(num_pages_pdf1, num_pages_pdf2):
    output_pdf.add_page(pdf2.pages[num_pages_pdf2 - 1 - i])

# Print a warning message if the pages of pdf1 are < than pdf2
if num_pages_pdf1 < num_pages_pdf2:
  print("Warning: PDF 1 has fewer pages than PDF 2.")

# Save the output file
with open(f"{args.output}", "wb") as file:
  output_pdf.write(args.output)
  print(f"{args.output} written.")
