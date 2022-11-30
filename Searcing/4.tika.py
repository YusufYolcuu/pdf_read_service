from tika import parser # pip install tika

raw = parser.from_file('./PDFS/b1.pdf')
print(raw['content'])