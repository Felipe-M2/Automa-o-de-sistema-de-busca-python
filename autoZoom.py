# > Automação de busca 
# - Busca por produtos em sites de compra

import requests
from bs4 import BeautifulSoup

url_base = 'https://www.zoom.com.br/search?q='

produto_nome = input('qual o produto/categoria procurar?')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('article', attrs={'class': 'Cell_Cell__1YAxR'})

for produto in produtos:

    titulo = produto.find('h2', attrs={'class': 'Text_Text___RzD- Text_LabelSmRegular__2Lr6I'})

    link = produto.find('a', attrs={'class': 'Cell_Content__1630r'})

    real = produto.find('strong', attrs={'class': 'Text_Text___RzD- Text_LabelMdBold__3KBIj CellPrice_MainValue__3s0iP'})

    imagen = produto.find('img', attrs={'class': 'Cell_Image__2-Jrs'})

    #print(produto.prettify())
    print('<div class="produto">')
    print('<a href=" https://www.zoom.com.br' + link['href'] + '">\n'
          '<img src="' + imagen['src'] + '" alt="">\n'
          '</a>'
    )
    print('<div class="preço">')
    print('<p class="titulo">', titulo.text + '</p>')
    print('<h4>', real.text + '</h4>')
    print('</div>')
    print('</div>')

    print('\n\n')