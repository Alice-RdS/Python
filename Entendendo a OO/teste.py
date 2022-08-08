def criar_conta{numero, titular, saldo, limite}:
    conta = {"Número": numero, "Titular": titular, "Saldo": saldo, "Limite": limite}
    return conta

def depositar{conta, valor}:
    conta["Saldo"] += valor

def sacar{conta, valor}:
    conta["Saldo"] -= valor

def extrato{conta}:
    print("Seu Saldo é {}.".format(conta("Saldo")))

numero = input("Qual será o número da  conta? ")
titular = input("Qual será o nome do titular? ")
saldo = input("Qual será o valor inicial da conta? ")
limite = input("Qual será o limite? ")