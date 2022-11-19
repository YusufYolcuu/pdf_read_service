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
        test = pdf.pq(bboxes[i]).text()
        dic[names[i]] = test
    return(dic)




pushdata('EN ALT','213.163, 601.569, 510.326, 1221.138')
pushdata('Test','48, 764, 134, 820')


print(pdfscrape(pdf,bboxes,names))