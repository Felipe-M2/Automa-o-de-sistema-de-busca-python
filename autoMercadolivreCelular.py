# > Automação de busca 
# - Busca por produtos em sites de compra

import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = input('qual o produto/categoria procurar?')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

for produto in produtos:

    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})

    link = produto.find('a', attrs={'class': 'ui-search-link'})

    real = produto.find('span', attrs={'class': 'price-tag-fraction'})

    #print(produto.prettify())
    print('<div class="produto">')
    print('<a href="', link['href'] + '">\n'
          '<img src="" alt="">\n'
          '</a>'
    )
    print('<div class="preço">')
    print('<p class="titulo">', titulo.text + '</p>')
    print('<h4>', real.text + '</h4>')
    print('</div>')
    print('</div>')

    print('\n\n')