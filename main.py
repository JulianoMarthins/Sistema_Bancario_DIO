# deposito, não pode depositar valores negativos

# saques, limite de 3 diários com 500 reais de limite por saque

# estrato contem todas as operações de saques e depositos, formatado com duas casas decimais e R$

print()
print("Bem vindo ao banco Money for nothing ".center(80))

menu = """
    Digite o número correspondente a sua escolha: 
        
        (1) => Deposito
        (2) => Saque
        (3) => Extrato
        (0) => Sair
 
    Digite sua opção:        
"""
LIMITE_SAQUE = 500 #Constante, valor não deve ser alterado
quantidade_saque = 3

extrato = ""
saldo = 0.0

while (True):
    print("=-" * 40)
    opcao = int(input(menu))
    print("=-" * 40)

    if (opcao == 0):
        print("Obrigado por visitar o Banco Money for Nothing".center(80))
        break

    elif (opcao == 1):
        valor = input("Digite o valor a depositar: ")
        valor = float(valor)

        if(valor > 0):
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}. Saldo atual R$ {saldo:.2f}\n"
        else:
            print("Valor de depósito inválido")

    elif (opcao == 2):
        if(quantidade_saque > 0):
            valor = input("Digite o valor a sacar: ")
            valor = float(valor)

            if(valor <= LIMITE_SAQUE and valor < saldo):
                saldo -= valor
                quantidade_saque -= 1
                extrato += f"Saque: R$ {valor:.2f}. Saldo atual: R$ {saldo:.2f}\n"

            else:
                print("Saque não autorizado, favor consultar a gerência")
        else:
            print("Limite de saque diários excedidos, duvidas, favor consultar a gerência")

    elif (opcao == 3):
        print(f"Extrato:".center(80))

        print(extrato)

    else:
        print("ERRO! \n Valor digitado é inválido")
