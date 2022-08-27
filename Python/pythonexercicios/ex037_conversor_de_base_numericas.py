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

n = int(input('Digite um número inteiro qualquer: '))

perfumaria('''Escolha a base de conversão: \n
1- Binário: \n
2- Octal: \n
3- Hexadecimail \n ''')

base = int(input('Escolha a base de conversão:'))

# [2:]Começa a partir do índice 2 e vai até o final da string, ou seja, elimina o zero e um, que são apenas
# para identificar que o valor apresentado será um binário, octal ou hexdeciaml

if base == 1:
    b = bin(n)
    perfumaria(f'O valor {n} convertido para binário é: {b[2:].upper()}') 
elif base == 2:
    o = oct(n)
    perfumaria(f'O valor {n} convertido para binário é: {o[2:].upper()}') 
elif base == 3:
    h = hex(n)
    perfumaria(f'O valor {n} convertido para binário é: {h[2:].upper()}')
else:
    print('Digite a opção 1, 2 ou 3!')