def jogar():
    from functools import total_ordering
    from importlib import import_module
    from random import random
    import telnetlib
    from termios import TCGETA
    from traceback import print_tb
    import random

    print("**************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("**************************")

    pontos = 100
    nivel_facil = 1
    nivel_medio = 2
    nivel_dificil = 3

    print("Escolha o nível de dificuldade: ")
    print("Fácil{}, Médio{}, Difícil{}:".format(nivel_facil,nivel_medio,nivel_dificil))

    nivel_escolhido = int(input("Escolha seu nível: "))

    #arredonda = random.random() * 10
    numero_secreto = random.randrange(11)
    tentativas = 3

    if (nivel_escolhido == nivel_facil):
        total_de_tentativas = 10
    elif (nivel_escolhido == nivel_medio):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3

    for rodada in range (1,total_de_tentativas + 1):
        chute_str = input("Digite seu chute, um número entre 1 e 10: ")
        chute = int(chute_str)
        acertou = (chute == numero_secreto)
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (chute < 1 or chute > 10):
            (print("Você deve digitar um número entre 1 e 10"))
            continue

        print("Tentativa: {} de {}".format(rodada,total_de_tentativas))
        if (acertou):
            print("Você acertou, PARABÉNS! ")
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            print("Você errou, que pena!")
            if (maior):
                print("Seu chute foi maior que o número secreto!")
            if (menor):
                print("Seu chute foi menor que o número secreto!")
        tentativas = tentativas - 1

    print("O número secreto era: ", numero_secreto)
    print("Sua pontuação total foi: {} ".format(pontos))
    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()
