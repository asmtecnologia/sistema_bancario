from collections import defaultdict

## Declaração de variáveis ##
deposito_total = 0
saque_total = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
AGENCIA = "0001"
clientes = defaultdict(dict)
contas = defaultdict(dict)
numero_conta = 0
LIMITE_SAQUES = 3

## Funções ##
def cad_clientes():
    cpf = int(input("Insira o CPF do cliente, apenas números: "))
    if cpf not in clientes.keys():
        clientes[cpf]["nome"] = input("Insira o nome do cliente: ")
        clientes[cpf]["nascimento"] = input("Insira a data de nascimento do cliente: ")
        clientes[cpf]["endereco"] = input("Endereço no formato logradouro, número - bairro - cidade/estado: ")
    else:
        print("Cliente já cadastrado!")

    return

def cad_conta():
    global numero_conta
    cpf = int(input("Insira o CPF do titular da conta: "))
    if cpf in clientes.keys():
        numero_conta += 1
        contas[numero_conta]["agencia"] = AGENCIA
        contas[numero_conta]["cpf"] = cpf
        for chave, valor in contas.items():
            print("Conta criada com sucesso!")
            print(f"Conta: {chave}")
            print(f"Agência e titular da conta: {valor}")
    else:
        print("Cliente não cadastrado!")      

    return

def func_deposito():
    global saldo
    global deposito_total
    deposito = float(input("Insira o valor que será depositado: "))
    if deposito > 0:
        saldo += deposito
        deposito_total += deposito
        print(f"Depósito no valor de R$ {deposito} realizado com sucesso!")
    else:
        print("O valor do depósito tem que ser um número positivo.")
    return

def func_saque():
    global limite
    global saldo
    global saque_total
    global numero_saques
    global LIMITE_SAQUES
    saque = float(input("Insira o valor que será sacado: "))
    if numero_saques < LIMITE_SAQUES:
        if saque < limite:
            if saldo > saque:
                saldo -= saque
                saque_total += saque
                numero_saques += 1
                print(f"Saque realizado no valor de R$ {saque}.")
            else:
                print("Saldo insuficiente para a realização do saque.")
        else:
            print("Valor limite para saque excedido!")
    else:
        print("Limite diário de saques excedido!")
    return

def func_extrato():
    global deposito_total
    global saque_total
    if deposito_total > 0:
        print(f"O valor total depositado foi de: R$ {deposito_total}.")
        if saque_total > 0:
            print(f"O valor total do saque foi de R$ {saque_total}.")
    elif saque_total > 0:
            print(f"O valor total do saque foi de R$ {saque_total}.")
    else:
            print("Não foram realizadas movimentações.")
            print(f"O saldo atual é de R$ {saldo}")
    return


menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar cliente
[5] Criar conta
[0] Sair

"""

## Lógica da aplicação ##
while True:

    opcao = int(input(menu))

    if opcao == 1:
        func_deposito()
    elif opcao == 2:
        func_saque()
    elif opcao == 3:
        func_extrato()
    elif opcao == 4:
        cad_clientes()
    elif opcao == 5:
        cad_conta()
    elif opcao == 0:
        break
    else:
        print("Opção inválida, favor selecione a operação desejada conforme abaixo:")

exit(0)