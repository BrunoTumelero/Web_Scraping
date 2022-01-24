from urllib.error import URLError
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
import csv

base = 'https://www.zattini.com.br/masculino/home?mi=ztt_mntop_masculino&psn=Menu_Top'
html = Request(base, headers={'User-Agent': 'Mozilla/5.0'})
url = urlopen(html).read()
bs = BeautifulSoup(url, 'html5lib')

class_link = []
#all categories
'''for link_class in bs.find_all('figure', {'class': 'categorias-figure'}):
    print(link_class.text)'''

for link_class in bs.find_all('li', {'class': 'drezzup-categorias-li'}):
    link = link_class.findChild('a')
    class_link.append(link.get('href'))

    #print(link)
#'https://www.zattini.com.br/calcados/masculino?mi=ztt_mntop_MASC-CAL-vermais&psn=Menu_Top&fc=menu'
pesq1 = 'https://www.zattini.com.br/calcados/masculino?mi=ztt_hm_masc_cat1_calcadosmasc&psn=Banner_BarradeCategorias_1masc&fc=barradecategorias'
html_pesq1 = Request(base, headers={'User-Agent': 'Mozilla/5.0'})
url_pesq1 = urlopen(html_pesq1).read()
bs_pesq1 = BeautifulSoup(url_pesq1, 'html5lib')
print('Pesquisando em:', pesq1)

for raw_data in bs_pesq1.find_all('div', {'class': 'item-list'}):
    print(raw_data)

