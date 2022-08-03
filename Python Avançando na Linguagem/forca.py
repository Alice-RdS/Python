def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "Iemanjá"
    letras_encontradas = ["_", "_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False

    print(letras_encontradas)

    while (not enforcou and not acertou): #Enquanto a sentença for verdadeira, irá rodar o while
        chute = input("Qual a letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.lower() == letra.lower()):
                letras_encontradas[index] = letra.lower()
            index = index + 1

        print(letras_encontradas)
        letras_faltando = str(letras_encontradas.count('_'))
        print('Ainda faltam {} letras'.format(letras_faltando))
        #else:
                #print("Não há letra {} na palavra.".format{letra})

        print("Jogando...")








    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
