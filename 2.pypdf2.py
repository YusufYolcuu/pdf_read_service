import PyPDF2

sample_pdf = open(r'./PDFS/b5.pdf', mode='rb')
pdfdoc = PyPDF2.PdfFileReader(sample_pdf)


page_one= pdfdoc.getPage(0)
print(page_one.extractText())