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

#############--Código Principal--#############################################################

perfumaria('Comparando números:')
print()
n1 = float(input(('Digite o primeiro valor: ')))
n2 = float(input(('Digite o segundo valor: ')))

if n1 == n2:
    perfumaria(f'{cores["roxo"]}Os dos valores {n1} e {n2} são iguais.{cores["limpa"]}')
elif n1 > n2:
    perfumaria(f'{cores["azul"]} {n1} é maior que {n2}.{cores["limpa"]}')
else:
    perfumaria(f'{cores["verde"]}{n2} é maior que {n1}{cores["limpa"]}')
