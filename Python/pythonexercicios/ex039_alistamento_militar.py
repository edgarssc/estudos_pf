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

def alistamento(nasc):
    dataAlistamento = nasc + 18
    return dataAlistamento

#############--Código Principal--#############################################################

from datetime import date
nasc = int(input('Informe seu ano de nascimento: '))
hoje = date.today().year
alistado = alistamento(nasc)

if alistamento(nasc) == hoje:
    perfumaria(f'Você deve se alistar esse ano {cores["roxo"]}IMEDIATAMENTE!{cores["limpa"]}')

elif (hoje - alistamento(nasc)) > 18:
    perfumaria(f'Você se alistou em {cores["azul"]}{alistado}{cores["limpa"]} há {cores["azul"]}{hoje - alistado}{cores["limpa"]}')

else:
    perfumaria(f'Faltam {cores["amarelo"]}{hoje - nasc} anos{cores["limpa"]} para seu alistamento militar.\n Seu alistamento será em {cores["amarelo"]}{18 - (hoje - nasc)} anos {cores["limpa"]}')
    