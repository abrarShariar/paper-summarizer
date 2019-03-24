import PyPDF2
# file path to research paper goes here
file_path = './papers/p20-legout.pdf'
pdfFileObj = open(file_path,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
