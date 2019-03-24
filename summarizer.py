# import PyPDF2
# # file path to research paper goes here
# file_path = './papers/p20-legout.pdf'
# pdfFileObj = open(file_path,'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# print(pdfReader.numPages)
# # get to a particular page
# pageObj = pdfReader.getPage(2)
# text_data = pageObj.extractText();
#
# print(text_data)

import io

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

import pdfminer
import sys

# print("Sys path: ", sys.path)
# exit()

# data mining shit goes here
def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    laparams = pdfminer.layout.LAParams()

    # setattr(laparams, "all_texts", True)
    # setattr(laparams, "detect_vertical", True)
    # setattr(laparams, "word_margin", 1.0)
    # setattr(laparams, "char_margin", 1.0)
    # setattr(laparams, "line_margin", 1.0)
    # setattr(laparams, "boxes_flow", 1.0)


    for param in ("all_texts", "detect_vertical", "word_margin", "char_margin", "line_margin", "boxes_flow"):
        paramv = locals().get(param, None)
        print("param: ", param)
        print("paramv: ", paramv)
        if paramv is not None:
            setattr(laparams, param, paramv)
        else:
            laparams = None

    # exit()


    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()

    if text:
        return text

if __name__ == '__main__':
    print(extract_text_from_pdf('./papers/p20-legout.pdf'))
