from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

html = Request('https://www.zattini.com.br/roupas/masculino?mi=ztt_hm_masc_cat2_roupasmas&psn=Banner_BarradeCategorias_2masc&fc=barradecategorias', headers={'User-Agent': 'Mozilla/5.0'})
url = urlopen(html)
bs = BeautifulSoup(url, "html5lib")
#print(bs.prettify())

def Itens():
    html_item = Request('https://www.zattini.com.br/camiseta-industrie-estampada-masculina-azul+petroleo-AD6-0481-879', headers={'User-Agent': 'Mozilla/5.0'})
    url_item = urlopen(html)
    bs_item = BeautifulSoup(url, "html5lib")
    raw_price = bs.find('div', {'class': 'default-price'}).find('strong')
    print(raw_price)

all_itens = bs.find('div', {'class': 'wrapper'}).find('a')
raw_data = bs.find_all('div', {'class': 'item-card__description__product-name'})
#Itens()
for link in bs.find('div', {'class': 'wrapper'}).find('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
#print(raw_data)
'''for data in raw_data:
    print(data.text)'''