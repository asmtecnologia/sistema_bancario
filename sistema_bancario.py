## Declaração de variáveis ##
deposito_total = 0
saque_total = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

## Lógica da aplicação ##
while True:

    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input("Insira o valor que será depositado: "))
        if deposito > 0:
            saldo += deposito
            deposito_total += deposito
            print(f"Depósito no valor de R$ {deposito} realizado com sucesso!")
        else:
            print("O valor do depósito tem que ser um número positivo.")
    elif opcao == 2:
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
    elif opcao == 3:
        if deposito_total > 0:
            print(f"O valor total depositado foi de: R$ {deposito_total}.")
            if saque_total > 0:
                print(f"O valor total do saque foi de R$ {saque_total}.")
        elif saque_total > 0:
            print(f"O valor total do saque foi de R$ {saque_total}.")
        else:
            print("Não foram realizadas movimentações.")
        print(f"O saldo atual é de R$ {saldo}")
    elif opcao == 0:
        break
    else:
        print("Opção inválida, favor selecione a operação desejada conforme abaixo:")

exit(0)