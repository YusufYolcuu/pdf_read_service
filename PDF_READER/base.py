import pdfquery


class PDFreader():
    # global variables
    page_number = 1
    titles_at_table = []
    values_at_table = []
    titles_at_table_two_columns = []
    values_at_table_two_columns = {}

    def __init__(self, pdf_name):
        # pdfquery library call
        self.pdf = pdfquery.PDFQuery(pdf_name)
        self.pdf.load()
        self.pdf.tree.write('test1.txt', pretty_print=True)

    def to_xmltag(self, bbox_pos):
        """the xml tag template have to be texted.
         And template is  'LTTextLineHorizontal:overlaps_bbox("48,  686,  300, 696")'
         take bbox position's values and returns the text"""
        return 'LTPage[pageid="{}"] LTTextLineHorizontal:overlaps_bbox("{}")'.format(self.page_number, bbox_pos)

    def next_page(self):
        self.page_number = self.page_number + 1

    def pdf_scrape(self, pdf, title_arr=None, value_arr=None, two_column_value=None):
        if value_arr is None:
            value_arr = PDFreader.values_at_table
        if title_arr is None:
            title_arr = PDFreader.titles_at_table
        if two_column_value is None:
            two_column_value = PDFreader.values_at_table_two_columns
        dic = {}

        # for one column value, add arrays to dictionary
        for i in range(len(title_arr)):
            if pdf.pq(value_arr[i]).text() != '':
                title = pdf.pq(title_arr[i]).text()
                value = pdf.pq(value_arr[i]).text()
                dic[title] = value
            else:
                print("there is not a value of this title. "
                      "the reasons of it maybe \n"
                      "    there is not a each character like that in pdf\n"
                      "    it is not a member of a table.\n"
                      "    or the table's template is different. more than 2 columns")
                print('-' * 60)

        # for two column. add values to dictionary
        for key in two_column_value:
            dic[key] = two_column_value[key]
        return dic
