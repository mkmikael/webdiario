__author__ = 'mikael'
# -*- coding: utf-8 -*-

import requests
from os import path
from scrapy.selector import Selector


def download_file(url, filepath):
    r = requests.get(url, stream=True)
    with open(filepath, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

def run():
    url_base = 'http://www.belem.pa.gov.br/diarioom'
    r = requests.get(url_base + '/index.jsf')
    selector = Selector(text=r.text, type="html")
    number = selector.xpath('//tbody[@id=\'grdDiario_data\']/tr/td[1]/text()').extract()
    date = selector.xpath('//tbody[@id=\'grdDiario_data\']/tr/td[2]/text()').extract()
    links = selector.xpath('//tbody[@id=\'grdDiario_data\']/tr/td[3]/a/@href').extract()
    for i in range(0, len(links)):
        local_filename = "/home/mikael/Documentos/diarios_oficial_belem/{0}.pdf".format(number[i])
        if path.isfile(local_filename):
            print("O diário {0} já existe".format(number[i]))
        else:
            print("Fazendo download do diario {0}...".format(number[i]))
            url_pdf = "{0}/{1}".format(url_base, links[i])
            download_file(url_pdf, local_filename)
            print("Download do diário {0} concluído!".format(number[i]))
