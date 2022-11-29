import pdfquery
from functions import *

pdf = pdfquery.PDFQuery('../PDFS/page1.pdf')
pdf.load()
pdf.tree.write('test1.txt', pretty_print=True)

# walk_on_page_check_value('35, 310, 200, 315', 20, 5)

""" 
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
push_data('35, 140, 223, 145') """



# y0 ile y1 arasında daima 6 değer fark olabilir. satır uzunluğu

push_data(find_bbox_of_title(pdf,'Taşınmaz Satış Kazancı İstisnası (K.V.K. Mad.'))

#          x0   y0   x1   y1
push_data('35, 280, 220, 286') # diğer indirimler cart curt ......
push_data('35,257, 220, 266')  # toplam yazısı x uzunluğu kısa burada check edilmeli
push_data('35, 275, 220, 281')
push_data(find_bbox_of_title(pdf,'Zarar'))
pdf_scrape(pdf)

# 35.0 257.7 64.997 266.7
