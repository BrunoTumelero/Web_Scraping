import site
from urllib import response
import requests
from bs4 import BeautifulSoup
import pandas as pd

pags = []
category = {}
product = []
price = []
discont = []
n = 1

def next_pages(n):
    all_pages = f'https://www.mercadolivre.com.br/ofertas?page={n}'
    conn_next_page = requests.get(all_pages)
    pags.append(all_pages)

def colect(n):
    pag = f'https://www.mercadolivre.com.br/ofertas?page={n}'
    connect_pag = requests.get(pag)
    site = BeautifulSoup(connect_pag.text, 'html5lib')
    print('Target: ', pag)
    for raw_product in site.find_all('p', {'class': 'promotion-item__title'}):
        product.append(raw_product.text)
    for raw_price in site.find_all('span', {'class': 'promotion-item__price'}):
        price.append(raw_price.text)
    for raw_discont in site.find_all('span', {'class': 'promotion-item__discount'}):
        discont.append(raw_discont.text)

    table = pd.DataFrame(list(zip(product, price, discont)), columns= ['Produtos', 'Preço', 'Desconto'])
    table.to_csv('products_mercado_livre.csv', '\t', 'utf8', index=False)
#coleted category
pag = str(f'https://www.mercadolivre.com.br/ofertas?page={n}')
connect_pag = requests.get(pag)
tg = BeautifulSoup(connect_pag.text, 'html5lib')
for cat in tg.find_all('a', {'class': 'list_element'}):
    category[cat.text] = cat.get('href')

next_pages(n)
if n <= len(pags):
    while 1:
        next_pages(n)
        colect(n)
        n += 1
            