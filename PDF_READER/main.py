import pdfquery
from functions import *

""" there are three functions that meaning is same as names of the functions. 
    push_data(): get position of searching word. adding to lists words and values
    get_value(): it is finding the value of title by position. 
    pdf_scrape(): when after you add to words which you want the values, you have to use this func. """

two_columns_titles_list = ["Taşınmaz Satış Kazancı İstisnası (K.V.K. Mad",
                           "İştirak Kazançları İstisnası (K.V.K Mad. 5/1-a)",
                           "Diğer İndirimler ve İstisnalar",
                           "Toplam",
                           "Kar ve İlaveler Toplamı",
                           "Cari Yıla Ait Zarar, İstisna ve İndirimler Toplamı"]


three_columns_titles_list = ["I. Dönen Varlıklar",
                             ". A. Hazır Değerler",
                             ". 1. Kasa",
                             ". 3. Bankalar"]


pdf = pdfquery.PDFQuery('../PDFS/beyanname.pdf')
pdf.load()
pdf.tree.write('test1.txt', pretty_print=True)


page_count = pdf.doc.catalog['Pages'].resolve()['Count']
for p in range(page_count):
    for title in two_columns_titles_list:
        push_data1(find_bbox_of_title(pdf, title))
    for title in three_columns_titles_list:
        push_data2(pdf, find_bbox_of_title(pdf, title))
    next_page()


pdf_datas = pdf_scrape(pdf)
for key in pdf_datas:
    print('-*-', key, '-->', pdf_datas[key])
