from datetime import date
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

#função para achar o menor valor na lista
def buscaMenor(lst):
    i = float("inf")
    for nr in lst:
        if nr < i:
            i = nr
    return i

#função para achar o maior valor na lista
def buscaMaior(lst):
    i = 0
    for x in lst:
        if x > i:
            i = x
    return i

#Carrega a data de hoje
data = date.today()
print('Date: {}'.format(data))

n1 = int(input('{}Digite o primeiro valor:{} '.format(cores['azul'],cores['limpa'])))
n2 = int(input('{}Digite o segundo valor:{} '.format(cores['amarelo'],cores['limpa'])))
n3 = int(input('{}Digite o terceiro valor:{} '.format(cores['verde'],cores['limpa'])))
lista = [n1,n2,n3]
menor = buscaMenor(lista)
maior = buscaMaior(lista)
print("O menor número digitado foi: {}{}{}".format(cores['amarelo'],menor,cores['limpa']))
print("O maior número digitado foi: {}{}{}".format(cores['azul'], maior, cores['limpa']))

