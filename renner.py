from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

base = 'https://www.lojasrenner.com.br/c/masculino/-/N-1xeiyoy'
links = []
n = 0
html = Request(base, headers={'User-Agent': 'Mozilla/5.0'})
url = urlopen(html)
bs = BeautifulSoup(url, "html5lib")
#print(bs.prettify())
#links dos produtos
for link in bs.find_all('a', {'class': 'ProductBox_productBox__1QP1S'}):
    links.append(link.get('href'))

raw_data = bs.find_all('span', {'class': 'ProductBox_title__s2Ufj'})

def get_information(n):
    html_base = 'https://www.lojasrenner.com.br'
    target = (html_base + links[n])
    print(target)
    site = Request(target, headers={'User-Agent': 'Mozilla/5.0'})
    url_target = urlopen(target)
    bs = BeautifulSoup(url_target, "html5lib")
    product_name = bs.find_all('h1', {'class': 'product_name'})
    product_price = bs.find_all('span', {'class': 'best_price'})
    for product in product_name:
        for price in product_price:
            print(f'Produto: {product.get_text().lstrip()}\nPreço: {price.text}')

while n < len(links):
    get_information(n)
    print(links[n])
    n += 1
