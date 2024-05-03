class Cliente:
    def __init__(self, nome, cpf, idade, rg):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.rg = rg

    def mostrar_dados(self):
        print(f"Nome: {self.nome} / CPF: {self.cpf} / Idade: {self.idade} / RG: {self.rg}")

