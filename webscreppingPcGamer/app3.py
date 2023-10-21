
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# Acessar site 
driver = webdriver.Chrome()
driver.get("https://www.novaliderinformatica.com.br/computadores-gamers")
#input() # Mantem o site aberto

# Pegar nome do produto
productName = driver.find_elements(By.XPATH,"//a[@class='nome-produto']")

# Pegar valor de preços
productPrice = driver.find_elements(By.XPATH,"//strong[@class='preco-promocional']")



# Criando a Planilha
workbook = openpyxl.Workbook()

# Criando a Aba 'produtos' na planilha
workbook.create_sheet('produtos')

# Selecionando a Aba 'produtos' na planilha
aba_produtos = workbook['produtos']

# Criando o cabeçalho da planilha
aba_produtos['A1'].value = 'Produto'
aba_produtos['B1'].value = "Preço"

# Obter data e hora da criação da planilha
data_e_hora = datetime.datetime.now()



# Truque para pegar somente produtos que tiver (nome e preço)
# Inserir nome de produtos e preços na Planilha Excel
for produto, preco in zip(productName, productPrice):
     aba_produtos.append([produto.text, preco.text])

# Obter data e hora da criação da planilha
data_e_hora = datetime.datetime.now()
data_e_hora_formatada = data_e_hora.strftime("%y-%m-%d_%H-%M-%S")

# Gerar um nome de arquivo único usando o timestamp atual
filename = f'produtos_{data_e_hora_formatada}.xlsx'

# Salvar dados em planilhas com o nome de arquivo único
workbook.save(filename)
print("Fim da execução")
