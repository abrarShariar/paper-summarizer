import PyPDF2
# file path to research paper goes here
file_path = './papers/p20-legout.pdf'
pdfFileObj = open(file_path,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
# get to a particular page
pageObj = pdfReader.getPage(2)
text_data = pageObj.extractText();

print(text_data)
