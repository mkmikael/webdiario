
__author__ = 'mikael'

import requests
import os
import json

from PyPDF2 import PdfFileReader

from datetime import datetime
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfpage import PDFPage
# from cStringIO import StringIO

# def convert_pdf_to_txt(path):
#     rsrcmgr = PDFResourceManager()
#     retstr = StringIO()
#     codec = 'utf-8'
#     laparams = LAParams()
#     device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
#     interpreter = PDFPageInterpreter(rsrcmgr, device)
#     fp = open(path, 'rb')
#     password = ""
#     maxpages = 0
#     caching = True
#     pagenos=set()
#     paginas = []
#     for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
#         paginas.append(retstr.getvalue())
#         retstr.truncate(0)
#         interpreter.process_page(page)
#     fp.close()
#     device.close()
#     retstr.close()
#     return paginas

def pdf_read_salvacao(path):
    pdf = PdfFileReader(open(path, 'rb'))
    print(pdf.getNumPages())
    print(pdf.getPage(0).extractText().split('\n'))

def insert_cloud(data):
    app_id = "uRkPJeVgTu1jbV3OSNNs5TixX33ulWPe8w8ZlewI"
    rest_key = "PZqT2xZLYsabsBKevU83VhHGbNWQSHyCo2UU8HDe"
    url_base = "https://api.parse.com/1/classes"
    headers = {
        "X-Parse-Application-Id": app_id,
        "X-Parse-REST-API-Key": rest_key,
        "Content-Type": "application/json"
    }
    requests.post(url_base + '/Diario', headers=headers, data=json.dumps(data))

path_base = '/home/mikael/Documentos/diarios_oficial_belem/'

# for file in os.listdir(path_base):
#     pages = convert_pdf_to_txt(path_base + file)
#     numero = file.replace('.pdf', '')
#     date = datetime.now().isoformat()
#     print("{0} Enviando...".format(numero))
#     for i, page in enumerate(pages):
#         data = {'content': page, 'data': {'iso': date, '__type': 'Date'}, 'numero': numero, 'page': i+1}
#         insert_cloud(data)
#     print("{0} Concluido!".format(numero))

pdf_read_salvacao(path_base + "12929.pdf")