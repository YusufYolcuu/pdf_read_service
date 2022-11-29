import pandas as pd

# global variables
titles_at_table = []
values_at_table = []


def get_value(pos):
    # Returns the value corresponding to the bbox location of the xml tag.
    pos_list = pos.split(',')
    # for add int casting
    pos_list[0] = str(int(pos_list[0]) + 465)  # y0
    pos_list[2] = str(int(pos_list[2]) + 340)  # y1
    # turn again list to text
    value_of_position = ""
    for i in range(len(pos_list)):
        value_of_position += pos_list[i] + ','
    # make the xml template form
    return to_xmltag(value_of_position[:-1])


def to_xmltag(bbox):
    """the xml tag template have to be texted.
     And template is  'LTTextLineHorizontal:overlaps_bbox("48,  686,  300, 696")'
     take bbox position's values and returns the text"""
    return 'LTTextLineHorizontal:overlaps_bbox("{}")'.format(bbox)


def push_data(bbox_title):
    # it gets the value from funcs. And push title and value to arrays. and return these
    # for using at pdf_scrape function, it has to be like xml tag(text form)
    titles_at_table.append(to_xmltag(bbox_title))
    # add to value to array
    values_at_table.append(get_value(bbox_title))


def pdf_scrape(pdf, title_arr, value_arr):
    dic = {}
    for i in range(len(title_arr)):

        title = pdf.pq(title_arr[i]).text()
        value = pdf.pq(value_arr[i]).text()

        print('-*-', pdf.pq(title_arr[i]).text(), pdf.pq(value_arr[i]).text())

        dic[title] = value
    return dic


def walk_on_page_check_value(bbx, y0=10, y1=15):
    bbx = bbx.split(',')
    i = bbx[3] if ((int(bbx[1]) // 10) < (int(bbx[3]) // 10)) else bbx[1]
    print(i)
    while (int(bbx[3]) // 10) != 0:
        bbx[1] = str(int(bbx[1]) - y0)
        bbx[3] = str(int(bbx[3]) - y1)
        bbox_new = ""
        for i in range(len(bbx)):
            bbox_new += bbx[i] + ','
        bbox_new = bbox_new[:-1]
        print(bbox_new)


def find_bbox_of_title(pdf, title):
    label = pdf.pq('LTTextLineHorizontal:contains({})'.format(title))
    print(label)
    left_corner = label.attr('x0')
    print(left_corner)
    # bottom_corner = float(label.attr('y0'))
    # name = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % ( left_corner, bottom_corner - 30, left_corner + 150, bottom_corner)).text()




