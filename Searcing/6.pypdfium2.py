import pypdfium2 as pdfium

pdf = pdfium.PdfDocument("foo.pdf")
version = pdf.get_version()  # get the PDF standard version
n_pages = len(pdf)  # get the number of pages in the document

page_indices = [i for i in range(n_pages)]  # all pages
renderer = pdf.render_to(
    pdfium.BitmapConv.pil_image,
    page_indices = page_indices,
    scale = 300/72,  # 300dpi resolution
)

print(pdf.get_toc)
n_digits = ""
for item in pdf.get_toc():  
    print('item')
    if item.n_kids == 0:
        state = "*"
    elif item.is_closed:
        state = "-"
    else:
        state = "+"
    
    if item.page_index is None:
        target = "?"
    else:
        target = item.page_index + 1
    
    print(
        "    " * item.level +
        "[%s] %s -> %s  # %s %s" % (
            state, item.title, target,
            pdfium.ViewmodeToStr[item.view_mode],
            [round(c, n_digits) for c in item.view_pos],
        )
    )