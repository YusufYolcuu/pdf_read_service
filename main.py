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
        print(type(text))
    return(dic)

def findvaluefromposition(pos):
    position = pos.split(',')
    position[1] = str(int(position[1]) + 400) #y0
    position[3] = str(int(position[3]) + 300) #y1

    positionew = ""
    for i in range(len(position)):
        positionew += position[i] + ','
    print(pos)
    print(positionew[:-1])
    return positionew[:-1]

findvaluefromposition('35, 300, 220, 350')

# pushdata('Taşınmaz satış kazancı', '35, 330.87, 220, 339.87')
pushdata('Taşınmaz satış değer'  , '500, 325.7, 560, 334.7')


# pushdata('İştirak kazançları istisnası'      , '35, 296.52, 220, 315.87')
# pushdata('İştirak kazançları istisnası değer', '500, 301.7, 560, 310.7')



# pushdata('Diğer indirimler ve istisnalar', '35, 277.7, 220, 286.7')
# pushdata('Diğer indirimler değer'        , '500, 277.7, 560, 286.7')



# pushdata('Toplam'      , '35, 257.7, 220, 266.7')
# pushdata('Toplam değer', '500, 257.7, 560, 266.7')



print(pdfscrape(pdf,bboxes,names))
