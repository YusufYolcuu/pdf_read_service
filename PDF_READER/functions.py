# global variables
titles_at_table = []
values_at_table = []

titles_at_table_two_columns = []
values_at_table_two_columns = {}
page_number = 1


def to_xmltag(bbox_pos):
    """the xml tag template have to be texted.
     And template is  'LTTextLineHorizontal:overlaps_bbox("48,  686,  300, 696")'
     take bbox position's values and returns the text"""
    return 'LTPage[pageid="{}"] LTTextLineHorizontal:overlaps_bbox("{}")'.format(page_number, bbox_pos)


def next_page():
    global page_number
    page_number = page_number + 1


# Returns the value corresponding to the bbox location of the xml tag.
# It is just for two columns table
def get_one_column_value(pos):
    pos_list = pos.split(',')
    # for add int casting
    pos_list[0] = str(int(pos_list[0]) + 465)  # x0
    pos_list[2] = str(int(pos_list[2]) + 340)  # x1
    # turn again list to text
    value_of_position = ""
    for i in range(len(pos_list)):
        value_of_position += pos_list[i] + ','
    # make the xml template form
    return to_xmltag(value_of_position[:-1])


def get_first_column_of_two_table(pos):
    pos_list = pos.split(',')
    # for add int casting
    pos_list[0] = str(int(pos_list[0]) + 335)  # x0
    pos_list[2] = str(int(pos_list[2]) + 240)  # x1
    # turn again list to text
    value_of_position = ""
    for i in range(len(pos_list)):
        value_of_position += pos_list[i] + ','
    # make the xml template form
    return to_xmltag(value_of_position[:-1])


def get_second_column_of_two_table(pos):
    pos_list = pos.split(',')
    # for add int casting
    pos_list[0] = str(int(pos_list[0]) + 480)  # x0
    pos_list[2] = str(int(pos_list[2]) + 390)  # x1
    # turn again list to text
    value_of_position = ""
    for i in range(len(pos_list)):
        value_of_position += pos_list[i] + ','
    # make the xml template form
    return to_xmltag(value_of_position[:-1])


# it gets the value from funcs. And pushes title and value to arrays. and returns these
# for using at pdf_scrape function, it has to be like xml tag(text form)
def push_data1(bbox_title):
    if bbox_title != 0:
        titles_at_table.append(to_xmltag(bbox_title))
        # add to value to array
        value = get_one_column_value(bbox_title)
        values_at_table.append(value)


def push_data2(pdf, bbox_title):
    if bbox_title != 0:
        titles_at_table_two_columns.append(pdf.pq(to_xmltag(bbox_title)).text())
        # add to value to array
        value1 = get_first_column_of_two_table(bbox_title)
        value2 = get_second_column_of_two_table(bbox_title)
        dictin = {}
        dictin['2012'] = pdf.pq(value1).text()
        dictin['2013'] = pdf.pq(value2).text()
        values_at_table_two_columns[pdf.pq(to_xmltag(bbox_title)).text()] = dictin


def pdf_scrape(pdf, title_arr=None, value_arr=None, two_column_value=None):
    if value_arr is None:
        value_arr = values_at_table
    if title_arr is None:
        title_arr = titles_at_table
    if two_column_value is None:
        two_column_value = values_at_table_two_columns
    dic = {}

    # for one column value
    for i in range(len(title_arr)):
        if pdf.pq(value_arr[i]).text() != '':
            title = pdf.pq(title_arr[i]).text()
            value = pdf.pq(value_arr[i]).text()
            # print('-*-', pdf.pq(title_arr[i]).text(), pdf.pq(value_arr[i]).text())
            dic[title] = value
        else:
            print('-' * 60, "\nthere is not a value of this title. "
                            "the reasons of it maybe \n"
                            "    there is not a each character like that in pdf\n"
                            "    it is not a member of a table.\n"
                            "    or the table's template is different. more than 2 columns")
            print('-' * 60)

    # for two column value
    for key in two_column_value:
        dic[key] = two_column_value[key]
    return dic


def find_bbox_of_title(pdf, title):
    # the function returns the bbox position of the title
    global bbox
    text = 'LTPage[pageid="' + str(page_number) + '"] LTTextLineHorizontal:contains("' + title + '")'
    label = pdf.pq(text)
    try:
        if len(label) > 1:
            # if the word count is more than one time
            for pq in range(len(label)):
                # print(pq.layout.get_text().strip(), title.strip())
                if label[pq].layout.get_text().strip() == title.strip():
                    x0 = float(label[pq].get('x0'))
                    y0 = float(label[pq].get('y0'))
                    # x1 = label[1].get('x1')
                    x1 = 220
                    y1 = float(label[pq].get('y1'))
                    bbox = str((int(x0))) + ',' + str(int(y0)) + ',' + str(int(x1)) + ',' + str(int(y1))
                else:
                    # for error catch
                    bbox = 0
            return bbox
        else:
            x0 = float(label.attr('x0'))
            y0 = float(label.attr('y0'))
            # x1 = float(label.attr('x1'))
            x1 = 220
            y1 = float(label.attr('y1'))
            bbox = str((int(x0))) + ',' + str(int(y0)) + ',' + str(int(x1)) + ',' + str(int(y1))
    except:
        bbox = 0
        # print('(' + title + ')\nthere is not a word or sentences like this at page', page_number)
    return bbox


def get_three_columns_title(pdf, title):
    pass


# ************************************ Test functions ********************************


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
