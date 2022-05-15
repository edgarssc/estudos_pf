def escolhe_jogo():

    from importlib import import_module
    import adivinhacao
    import forca

    print("**************************")
    print("Escolha seu jogo !")
    print("**************************")

    numero_do_jogo_forca = 1
    numero_do_jogo_adivinhacao = 2
    print("{} Forca ou {} Adivinhação:".format(numero_do_jogo_forca,numero_do_jogo_adivinhacao))
    jogo = int(input("Escolha seu jogo? "))

    if (jogo == 1):
        print("Jogando Forca!")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando Adivinhação!")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()