def criar_conta{numero, titular, saldo, limite}:
    conta = {"Número": numero, "Titular": titular, "Saldo": saldo, "Limite": limite}
    return conta

def depositar{conta, valor}:
    conta["Saldo"] += valor

def sacar{conta, valor}:
    conta["Saldo"] -= valor

def extrato{conta}:
    print("Seu Saldo é {}.".format(conta("Saldo"))