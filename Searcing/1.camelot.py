import camelot

# tables = camelot.read_pdf('foo.pdf')
# foo deneme pdfindeki table ı okuyor ama beyannamalerdeki tabloları opkumuyorç.
tables = camelot.read_pdf('./PDFS/b1.pdf')
print(tables)
# print(tables[0].df)

def toexcell():
    tables.export('foo.csv', f='csv', compress=True) # json, excel, html, markdown, sqlite
    tables[0]
    tables[0].parsing_report
    {
        'accuracy': 99.02,
        'whitespace': 12.24,
        'order': 1,
        'page': 1
    }
    tables[0].to_csv('foo.csv') # to_json, to_excel, to_html, to_markdown, to_sqlite
    tables[0].df # get a pandas DataFrame!