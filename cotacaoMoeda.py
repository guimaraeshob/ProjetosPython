from tkinter import *
import requests
from bs4 import BeautifulSoup

def dolar():
    site = requests.get("https://www.google.com/finance/quote/USD-BRL?sa=X&ved=2a")
    soup = BeautifulSoup(site.content, 'html.parser')
    #print(soup.prettify())
    dolar = soup.find('div',{'class':'YMlKec fxKbKc'}).get_text().strip()
    #print('Dolar hoje: ',dolar)
    texto_cotacao["text"] = dolar
    
def euro():
    site2 = requests.get("https://www.google.com/finance/quote/EUR-BRL?sa=X&ved=2ahUKEwiv8LenqqD9AhX3LbkGHbhiDE0QmY0JegQIBhAd")
    soup2 = BeautifulSoup(site2.content, 'html.parser')
    euro = soup2.find('div',{'class':'YMlKec fxKbKc'}).get_text().strip()
    texto_cotacao2["text"] = euro
    #print('Euro hoje: ',euro)
    
    


app = Tk() # inicia a jenala 
app.geometry("400x200")

app.title('Cotação atual do dolar') # titulo da janela 

texto_orientacao = Label(app, text="Clique no botão") # texto de orientação para o usuário
texto_orientacao.grid(column=1, row=1) # mostra onde o texto irá aparecer 

btn = Button(app, text="Cotação Dolar",command=dolar) # Cria o botão e chamando a função 
btn.grid(column=1, row=3) # Chama o botão na interface

btn2 = Button(app, text="Cotação Euro", command=euro)
btn2.grid(column=2, row=3)

texto_cotacao = Label(app, text="")
texto_cotacao.grid(column=1, row=5)

texto_cotacao2 = Label(app, text="")
texto_cotacao2.grid(column=2, row=5)

app.mainloop() # mantem a janela aberta

print("Open aplication...")

