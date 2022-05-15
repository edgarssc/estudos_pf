import random
def jogar():

    mensagem_boas_vindas()
    palavra_secreta = carrega_palavras_secretas()
 
    venceu = False
    perdeu = False
    erros = 0

    tamanho_da_palavra = len(palavra_secreta)
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    
    print("A palavra possui {} letras!".format(tamanho_da_palavra))
    print(letras_acertadas)

    #Enquanto não venceu nem perdeu
    while (not venceu and not perdeu):
        chute = pede_chute()
        if (chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1 
            desenha_forca(erros)
        perdeu = erros == 6
        venceu = "_" not in letras_acertadas
        print(letras_acertadas)
    print("Fim do jogo")

    if (venceu):
        imprime_msm_vencedor()
    else:
        imprime_msn_perdedor(palavra_secreta)
    
def mensagem_boas_vindas():
    print("**************************")
    print("Bem vindo ao jogo da Forca!")
    print("**************************")

def carrega_palavras_secretas():
    arquivo = open("entrada.txt","r")
    palavras =[]
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letras in palavra]

def pede_chute():
    chute = input("Digite a letra do seu chute: ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    posicao = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[posicao] = letra
        posicao += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_msm_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_msn_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if (__name__ == "__main__"):
    jogar()