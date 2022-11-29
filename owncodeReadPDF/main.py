import pdfquery
from functions import *

pdf = pdfquery.PDFQuery('../PDFS/page1.pdf')
pdf.load()
pdf.tree.write('test1.txt', pretty_print=True)

# walk_on_page_check_value('35, 310, 200, 315', 20, 5)

push_data('35, 330, 200, 339')
push_data('35, 300, 200, 315')
push_data('35, 280, 200, 286')
push_data('35, 257, 200, 266')
push_data('35, 236, 205, 245')
push_data('35, 221, 223, 230')
push_data('35, 210, 223, 215')
push_data('35, 200, 223, 205')
push_data('35, 180, 223, 190')
push_data('35, 170, 223, 175')
push_data('35, 150, 223, 160')
push_data('35, 140, 223, 145')

pdf_scrape(pdf, titles_at_table, values_at_table)
find_bbox_of_title(pdf, 'Kar')