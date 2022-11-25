import pdfquery
import pandas as pd

# global variables
bboxes = []
values = []

def findvaluefromposition(pos):
    position = pos.split(',')
    position[0] = str(int(position[0]) + 465) #y0
    position[2] = str(int(position[2]) + 340) #y1

    positionew = ""
    for i in range(len(position)):
        positionew += position[i] + ','
    return positionew[:-1]

def addxmltagbbox(bbox) :
    test = '"'+bbox+'"'
    bbox = 'LTTextLineHorizontal:overlaps_bbox(' + test + ')'
    return  bbox

def pushdata(bbox):
    box = bbox
    bbox = addxmltagbbox(bbox)
    box = findvaluefromposition(box)
    box = addxmltagbbox(box)

    bboxes.append(bbox)
    values.append(box)
    return bbox,box

def pdfscrape(pdf,bboxes,values):
    dic ={}
    for i in range(len(bboxes)):
        title = pdf.pq(bboxes[i]).text()
        value = pdf.pq(values[i]).text()
        print('-*-',pdf.pq(bboxes[i]).text(),pdf.pq(values[i]).text())
        dic[title] = value
    return(dic)



def walkonpdf_checkkeyvalue(bbx,y0=10,y1=15):
    bbx = bbx.split(',')
    i = bbx[3] if ( (int(bbx[1])//10) < (int(bbx[3])//10) ) else bbx[1]
    print(i)
    while((int(bbx[3])//10) != 0):
        bbx[1] = str(int(bbx[1])-y0)
        bbx[3] = str(int(bbx[3])-y1)
        bboxnew = ""
        for i in range(len(bbx)):
            bboxnew += bbx[i] + ','
        bboxnew = bboxnew[:-1]  
        



def findbboxoftile(title):
    pass
def findkeysoftitle():
    pass

def walkony0(x):
    return str(int(x[1])-20)
    
def walkony1(x):
    return str(int(x[3])-10)
    