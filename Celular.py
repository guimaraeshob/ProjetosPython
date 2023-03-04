import requests
from bs4 import BeautifulSoup
import time
import csv

url = "https://lista.mercadolivre.com.br/celular-usado#D[A:celular%20usado]"
site =  requests.get(url)
soup = BeautifulSoup(site.content, "html.parser")
#print(soup.prettify())

# Abrir um aquivo csv para gravar os dados
with open('produto.csv', mode='w', newline='') as file:

    # Cria um objeto write CSV
    writer = csv.writer(file,delimiter=',')

    # Escreve o cabeçalho da tabela
    writer.writerow(['Nome do Produto','Preço'])

    # Loop através dos produtos encontrado com Beautifulsoup
    for produto in soup.find('ol',{'class':'ui-search-layout ui-search-layout--stack shops__layout'}):
        nomeCel = produto.find('h2',{'class':'ui-search-item__title shops__item-title'}).text
        precoCel = produto.find('span',{'class':'price-tag-fraction'}).text

        # Escreve uma nova linha no arquivo CSV com o nome e preço do produto
        writer.writerow([nomeCel,precoCel])






