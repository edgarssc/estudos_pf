#####################--Cores--#############################################################

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

#############--Funções--#####################################################################

def perfumaria(X):
    print('-='*40)
    print(X)
    print('-='*40)

def idade(nasc):
    idade = date.today().year - nasc
    return idade
#testando funções com o uso de lambda - funções anônimas
idade2 = lambda x: date.today().year - x

#############--Código Principal--#############################################################

from datetime import date

nasc = int(input('Informe seu ano de nascimento: '))
hoje = date.today().year

if  idade(nasc) <= 9:
    perfumaria(f'Você é um atleta {cores["amarelo"]}MIRIM{cores["limpa"]}')
elif  (idade2(nasc) > 9) and (idade(nasc) <= 14):
    perfumaria(f'Você é um atleta {cores["azul"]}INFANTIL{cores["limpa"]}')
elif  (idade(nasc) > 14) and (idade(nasc) <= 19):
    perfumaria(f'Você é um atleta {cores["roxo"]}JUNIOR{cores["limpa"]}')
elif  (idade(nasc) > 19) and (idade(nasc) <= 25):
    perfumaria(f'Você é um atleta {cores["verde"]}SÊNIORL{cores["limpa"]}')
else:
    perfumaria(f'Você é um atleta {cores["vermelho"]}MASTER{cores["limpa"]}')