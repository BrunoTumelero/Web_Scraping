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

for link_class in bs.find_all('figure', {'class': 'categorias-figure'}):
    link = link_class.findChildren('a')
    class_link.append(link[0].get('href'))

print(class_link)
