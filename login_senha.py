from tkinter import *

janela = Tk()

janela.title("Login")
janela.geometry('200x150')
usuario = Label(janela, text='Usuário:').grid(row=0)
senha = Label(janela, text='senha:').grid(row=1)

input_usuario = Entry(janela).grid(row=0, column=2,padx=5, pady=10, sticky=W)
input_senha = Entry(janela).grid(row=1, column=2, padx=5, pady=10, sticky=W)

cmd_login = Button(janela, text='Login').grid(row=3, column=2, sticky=E)


janela.mainloop()