import pdfquery
import pandas as pd

pdf = pdfquery.PDFQuery('page1.pdf')
pdf.load()
pdf.tree.write('test1.txt', pretty_print = True)

bboxes = []
names = []

def pushdata(name,bbox,bboxes=bboxes,names=names):
    test = '"'+bbox+'"'
    bbox = 'LTTextLineHorizontal:overlaps_bbox(' + test + ')'
    bboxes.append(bbox)
    names.append(name)

def pdfscrape(pdf,bboxes,names):
    dic ={}
    for i in range(len(bboxes)):
        text = pdf.pq(bboxes[i]).text()
        dic[names[i]] = text
        print(text)
    return(dic)




pushdata('Taşınmaz satış kazancı', '35.0, 330.87, 221.381, 339.87')
pushdata('Taşınmaz satış değer'  , '514.98, 325.7, 559.998, 334.7')


pushdata('İştirak kazançları istisnası'      , '35.0, 296.52, 216.395, 315.87')
pushdata('İştirak kazançları istisnası değer', '519.99, 301.7, 560.004, 310.7')



pushdata('Diğer indirimler ve istisnalar', '35.0, 277.7, 146.465, 286.7')
pushdata('Diğer indirimler değer'        , '514.98, 277.7, 559.998, 286.7')



pushdata('Toplam'      , '35.0, 257.7, 64.997, 266.7')
pushdata('Toplam değer', '514.98, 257.7, 559.998, 266.7')



print(pdfscrape(pdf,bboxes,names))
