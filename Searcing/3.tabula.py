import tabula

df = tabula.read_pdf("foo.pdf",pages='all', stream = True)

print(df)
# output = "test1.csv"
# tabula.convert_into(df, output, output_format="csv", stream=True)
df = tabula.read_pdf("./PDFS/b1.pdf",pages='all', stream = True)
print('*'*100)
print(df)