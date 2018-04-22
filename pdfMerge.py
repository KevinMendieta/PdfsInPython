import PyPDF2

def get_file(fileName):
	return open(fileName, 'rb')

def create_pdf_file():
	return open("new.pdf", 'wb')

def get_reader(pdfFile):
	return PyPDF2.PdfFileReader(pdfFile)

def get_writer():
	return PyPDF2.PdfFileWriter()

def get_pdf_pages(pdf):
	pages = []
	for index in range(pdf.getNumPages()):
		pages.append(pdf.getPage(index))
	return pages

def add_pages(pages, pdfWriter):
	for page in pages:
		pdfWriter.addPage(page)
	return pdfWriter

def merge_pdfs(firstPdf, secondPdf, pdfWriter):
	firstPages = get_pdf_pages(firstPdf)
	secondPages = get_pdf_pages(secondPdf)
	add_pages(firstPages, pdfWriter)
	add_pages(secondPages, pdfWriter)
	return pdfWriter


"""
Simple Example

first_file = get_file("pdf-test1.pdf")
second_file = get_file("pdf-test2.pdf")

first_pdf = get_reader(first_file)
second_pdf = get_reader(second_file)

pdf_writer = get_writer()
out_file = create_pdf_file()

merge_pdfs(first_pdf, second_pdf, pdf_writer)
pdf_writer.write(out_file)

first_file.close()
second_file.close()
out_file.close()
"""

