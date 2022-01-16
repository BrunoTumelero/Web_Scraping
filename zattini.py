from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

html = Request('https://www.zattini.com.br/roupas/masculino?mi=ztt_hm_masc_cat2_roupasmas&psn=Banner_BarradeCategorias_2masc&fc=barradecategorias', headers={'User-Agent': 'Mozilla/5.0'})
url = urlopen(html)
bs = BeautifulSoup(url, "html5lib")
#print(bs.prettify())

raw_data = bs.find_all('div', {'class': 'item-card__description__product-name'})
raw_price = bs.find_all('data-price = price')
print(raw_price)
#print(raw_data)
'''for data in raw_data:
    print(data.text)'''