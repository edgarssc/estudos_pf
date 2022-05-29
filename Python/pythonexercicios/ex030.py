cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'amarelo':'\033[1;33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'roxo':'\033[1;35m'}

cores_fundo = {'limpa':'\033[m',
         'azul':'\033[1;44m',
         'amarelo':'\033[1;43m',
         'pretoebranco':'\033[7;40m',
         'vermelho':'\033[1;41m',
         'verde':'\033[1;42m',
         'roxo':'\033[1;45m'}

n = int(input("Digite um número inteiro:"))
if n %2 == 0:
    print("O número {} é um número {}PAR!{}".format(n, cores['azul'], cores['limpa']))
else:
    print("O número {} é um número {}IMPAR!{}".format(n,cores['amarelo'],cores['limpa']))