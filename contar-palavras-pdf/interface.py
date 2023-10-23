import PyPDF2
import tkinter as tk
from tkinter import filedialog

def contar_palavra_em_pdf(pdf_file, palavra):
    # Abra o arquivo PDF em modo de leitura binária
    with open(pdf_file, 'rb') as pdf:
        # Crie um objeto PDFReader
        pdf_reader = PyPDF2.PdfReader(pdf)

        # Inicialize uma variável para contar as ocorrências da palavra
        contagem = 0

        # Itere pelas páginas do PDF
        for page_num in range(len(pdf_reader.pages)):
            # Obtenha o texto da página
            page = pdf_reader.pages[page_num]
            texto = page.extract_text()

            # Quebre o texto em palavras e conte as ocorrências da palavra desejada
            palavras = texto.split()
            contagem += palavras.count(palavra)

        return contagem

def buscar_arquivo():
    file_path = filedialog.askopenfilename()
    entry_arquivo.delete(0, tk.END)
    entry_arquivo.insert(0, file_path)

def contar_palavra():
    pdf_file = entry_arquivo.get()
    palavra = entry_palavra.get()
    ocorrencias = contar_palavra_em_pdf(pdf_file, palavra)
    resultado_label.config(text=f'A palavra "{palavra}" aparece {ocorrencias} vezes no PDF.')

# Configuração da janela
window = tk.Tk()
window.title("Contador de Palavras em PDF")
window.geometry("400x300")

# Botão para selecionar o arquivo PDF
selecionar_arquivo_button = tk.Button(window, text="Selecionar Arquivo PDF", command=buscar_arquivo)
selecionar_arquivo_button.pack(pady=20)

# Entrada de arquivo e palavra
entry_arquivo = tk.Entry(window, width=60)
entry_arquivo.pack()

label_palavra = tk.Label(window, text="Palavra a ser procurada:")
label_palavra.pack(pady=10)

entry_palavra = tk.Entry(window, width=60)
entry_palavra.pack(pady=10)

# Botão para contar as ocorrências
contar_button = tk.Button(window, text="Contar Ocorrências", command=contar_palavra)
contar_button.pack()

# Resultado
resultado_label = tk.Label(window, text="")
resultado_label.pack()

window.mainloop()
