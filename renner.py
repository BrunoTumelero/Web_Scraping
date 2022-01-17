from urllib.error import URLError
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
import csv

base = 'https://www.lojasrenner.com.br/c/masculino/-/N-1xeiyoy'
next_page = '?page='
links = []
n = 0
number_pages = 2
all_products = []
all_price = []

def request_html(base, number):
    try:
        page = str(number)
        new_target = str(base + '?page=' + page)
        html = Request(base, headers={'User-Agent': 'Mozilla/5.0'})
        url = urlopen(html).read()
        bs = BeautifulSoup(url, "html5lib")
        #links dos produtos
        for link in bs.find_all('a', {'class': 'ProductBox_productBox__1QP1S'}):
            links.append(link.get('href'))
    except URLError:
        request_html(base, number_pages)

def get_information(n):
    try:
        html_base = 'https://www.lojasrenner.com.br'
        target = (html_base + links[n])
        site = Request(target, headers={'User-Agent': 'Mozilla/5.0'})
        url_target = urlopen(target)
        bs = BeautifulSoup(url_target, "html5lib")
        product_name = bs.find_all('h1', {'class': 'product_name'})
        product_price = bs.find_all('span', {'class': 'best_price'})
        for raw_product in product_name:
            for raw_price in product_price:
                product = raw_product.text.lstrip()
                price = raw_price.text
                all_products.append(product)
                all_price.append(price)
                table = pd.DataFrame(list(zip(all_products, all_price)), columns=['Produto', 'Valor'])
                print(table)
                table.to_csv('products_renner.csv', '\t', encoding='utf8', index=False)
    except URLError:
        get_information(n)
            
html = Request(base, headers={'User-Agent': 'Mozilla/5.0'})
url = urlopen(html)
bs = BeautifulSoup(url, "html5lib")
#links dos produtos
for link in bs.find_all('a', {'class': 'ProductBox_productBox__1QP1S'}):
    links.append(link.get('href'))

while n < len(links):
    request_html(base, number_pages)
    get_information(n)
    n += 1
    number_pages += 1
