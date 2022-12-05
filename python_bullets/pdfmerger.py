from PyPDF2 import PdfMerger
import sys
file = sys.argv[1:]
def func_merge(pro):
  merger = PdfMerger()
  for pdf in file:
    merger.append(pdf)
  merger.write("merged-pdf.pdf")
func_merge(file)

	