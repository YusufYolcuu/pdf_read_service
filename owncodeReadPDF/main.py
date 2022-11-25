import pdfquery
from functions import *


pdf = pdfquery.PDFQuery('../PDFS/page1.pdf')
pdf.load()
pdf.tree.write('test1.txt', pretty_print = True)




# walkonpdf_checkkeyvalue('35, 310, 200, 315',20,5)




pushdata('35, 330, 200, 339')
pushdata('35, 300, 200, 315')
pushdata('35, 280, 200, 286')
pushdata('35, 257, 200, 266')
pushdata('35, 236, 127, 245')
pushdata('35, 221, 223, 230')
pushdata('35, 210, 223, 215')
pushdata('35, 200, 223, 205')
pushdata('35, 180, 223, 190')
pushdata('35, 170, 223, 175')
pushdata('35, 150, 223, 160')
pushdata('35, 140, 223, 145')
pdfscrape(pdf,bboxes,values)

