import  PyPDF2 
pdf1 = PyPDF2.PdfFileReader( open('mergedpdf.pdf', 'rb'))
pdf2 = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output =  PyPDF2.PdfFileWriter()
for i in range (pdf1.getNumPages()):
    page = pdf1.getPage(i)
    page.mergePage(pdf2.getPage(0))
    output.addPage(page)

with open('merged_file.pdf','wb') as merged_file:
    output.write(merged_file)