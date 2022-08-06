import random

def jogar():
    apresenta()
    palavra_secreta = configura()
    letras_encontradas = fruta(palavra_secreta)
    print(letras_encontradas)
    play(palavra_secreta, letras_encontradas)

def apresenta():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def configura():
    arquivo = open("frutas2.txt", "r")
    frutas = []

    for linha in arquivo:
        linha = linha.strip()
        frutas.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(frutas))
    palavra_secreta = frutas[numero]
    return palavra_secreta

def fruta(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def play(palavra_secreta, letras_encontradas):

    enforcou = False
    acertou = False
    chances = 0

    while (not enforcou and not acertou): #Enquanto a sentença for verdadeira, irá rodar o while
        chute = input("Qual a letra? ")
        chute = chute.strip().lower()
        palavra_secretalower = palavra_secreta.lower()

        if (chute in palavra_secretalower):
            index = 0
            for letra in palavra_secreta:
                if(chute.lower() == letra.lower()):
                    letras_encontradas[index] = letra
                index += 1

            print(letras_encontradas)
            acertou = "_" not in letras_encontradas

            if (acertou):
                print("Você fugiu da Forca!")
                break

            letras_faltando = str(letras_encontradas.count('_'))
            print('Ainda faltam {} letras'.format(letras_faltando))

            print("Jogando...")
        else:
            print("Não há letra {} na palavra.".format(chute))
            chances += 1
            enforcou = chances == 6
            if(enforcou):
                print("Você foi enforcado! A fruta era {}!" .format(palavra_secreta))

if(__name__ == "__main__"):
    jogar()
