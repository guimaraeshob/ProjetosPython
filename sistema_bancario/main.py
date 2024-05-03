from sistema_bancario import Conta
from cliente import Cliente

# Cliente
nome = str(input("Informe o nome: "))
cpf = int(input("Informe o CPF: "))
idade = int(input("Informe a idade: "))
rg = int(input("Informe o RG: "))

usuario1 = Cliente(nome, cpf, idade, rg)

# Conta
num_conta = str(input("A respeito de sua conta, informe o número da mesma: "))
saldo = int(input("Informe seu saldo: "))

conta1 = Conta(usuario1, num_conta, saldo)

print(f"Seja bem-vindo(a) {usuario1.nome}, de conta de número {conta1.num_conta}.")

respondendo = True

while respondendo:
    opcao = int(input("\n"'''O que deseja fazer?
    1 - Saque
    2 - Depósito
    3 - Saldo
    4 - Meus Dados
    5 - Sair
    
Opção: '''))

    if opcao == 1:
        valor = int(input(f"Quanto deseja sacar do seu saldo de {conta1.saldo}? "))
        conta1.saque(valor)
    elif opcao == 2:
        valor = int(input(f"Quanto deseja depositar? "))
        conta1.deposito(valor)
    elif opcao == 3:
        conta1.mostrar_saldo()
    elif opcao == 4:
        usuario1.mostrar_dados()
    elif opcao == 5:
        print("Obrigado! Até a próxima.")
        break
    else:
        print("Opção inválida, tente novamente.")
