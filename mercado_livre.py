import site
from urllib import response
import requests
from bs4 import BeautifulSoup
import pandas as pd


base = 'https://www.mercadolivre.com.br/'
res = requests.get(base)
bs = BeautifulSoup(res.text, 'html5lib')
links_utils = []
category = {}
product = []
price = []
discont = []
n = 0

def next_pages(n):
    all_category = str(f'https://www.mercadolivre.com.br/ofertas?page={n}')
    conn_next_page = requests.get(all_category)
    np = BeautifulSoup(conn_next_page.text, 'html5lib')
    for link in np.find_all('li', {'class': 'andes-pagination__button'}):
        print('Pagina: ', all_category)

def colect(n):
    pag = str(f'https://www.mercadolivre.com.br/ofertas?page={n}')
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

pag = str(f'https://www.mercadolivre.com.br/ofertas?page={n}')
connect_pag = requests.get(pag)
tg = BeautifulSoup(connect_pag.text, 'html5lib')
for cat in tg.find_all('a', {'class': 'list_element'}):
    category[cat.text] = cat.get('href')
    print(category)
'''v = 1
while v:
    if n in 
    try:
        colect(n)
        n += 1
    except:
        v = 0'''


            
            