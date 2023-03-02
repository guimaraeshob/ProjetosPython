import cv2
import time
import pytesseract
from tkinter import* 
from tkinter import filedialog


def imgNf():

    # Escolhe a imagem em qualquer diretório
    file_path = filedialog.askopenfilename()
    print(file_path)
    
    # Ler a imagem
    imagem = cv2.imread(file_path)
    time.sleep(1)
    
    # Configuração do Tesseract para rodar no windows 
    caminho = r"C:\Users\notehp\AppData\Local\Programs\Tesseract-OCR"
    pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
    texto = pytesseract.image_to_string(imagem)
    time.sleep(1)
    
    # Salva os dados da NF em um arquivo .txt
    nome_arquivo = "arquivo_"+ str(int(time.time())) + ".txt"
    file = open(nome_arquivo,"w")
    file.write(texto)
    file.close()


    lb2["text"] = texto
    aviso1["text"] = "Dados da NF extraido com sucesso !"
    
   

    


janela = Tk() # Abre janela

btn = Button(janela,
             width=10,
             text="Ler a imagem",
             padx=10,
             command=imgNf
)
btn.place(x=20, y=20)

lb2 = Label(janela,
            text = "Mostra dados extraidos...",
            justify="left"
)
lb2.place(x=10, y=100)


aviso1 = Label(janela,
               justify="left",
               text=""
)
aviso1.place(x=20, y=60)


janela.geometry("420x600") # Tamanho geral da tela
janela['background']='#F8F8FF'

janela.mainloop() # Mantem janela aberta

