def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("frutas.txt", "r")
    arquivo = arquivo.strip[]
    palavra_secreta = "Iemanjá"
    letras_encontradas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    chances = 0

    print(letras_encontradas)

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
                print("Você foi enforcado!")
                break



if(__name__ == "__main__"):
    jogar()
