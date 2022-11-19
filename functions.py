import PyPDF2

def show_all_pages(pdfReader):
    for page in range(pdfReader.numPages):
        print('*'*50,page+1,'*'*50)
        print('\n\n')
        pageObj = pdfReader.getPage(page)
        print(pageObj.extractText())
        
def show_page(pdfReader,page):
    pageObj = pdfReader.getPage(page-1)
    print(pageObj.extractText())
