import PyPDF2

PDF_SOURCE = './raw-pdfs/'
PDF_DESTINATION = './fnal-pdfs-result/'


def pdf_Tilter():
    with open(f'{PDF_SOURCE}/dummy.pdf', 'rb') as pdf1:
        reader = PyPDF2.PdfFileReader(pdf1)
        page = reader.getPage(0)
        page.rotateCounterClockwise(90)

        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        with open(f'{PDF_DESTINATION}/tilt.pdf', 'wb') as pdfTilt:
            writer.write(pdfTilt)


def combiner_PDF(*args):
    merger = PyPDF2.PdfFileMerger()
    destination = f'{PDF_DESTINATION}three-files-merge.pdf'

    for pdf in args:
        fullpdf = f'{PDF_SOURCE}{pdf}'
        merger.append(fullpdf)
    merger.write(destination)


def watermark_PDF():
    template = PyPDF2.PdfFileReader(f'{PDF_SOURCE}super.pdf', 'rb')
    watermark = PyPDF2.PdfFileReader(f'{PDF_SOURCE}wtr.pdf', 'rb')
    output = PyPDF2.PdfFileWriter()

    pages = template.getNumPages()
    for i in range(pages):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        with open(f'{PDF_DESTINATION}watermark_output.pdf', 'wb') as file:
            output.write(file)


# pdf_Tilter()
#combiner_PDF('dummy.pdf', 'twopage.pdf', 'wtr.pdf')
watermark_PDF()
