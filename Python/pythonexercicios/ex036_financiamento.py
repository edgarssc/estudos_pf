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
    print('-='*20)
    print(X)
    print('-='*20)

#############--Código Principal--#############################################################

vcasa = float(input('Qual o valor da casa: '))
scomprador = float(input('Qual o salário do comprador: '))
anos = int(input('Quantos anos a casa será financiada: '))
meses = float(anos * 12)
prestacao = (vcasa / meses)
limite = scomprador * 0.3

if prestacao >= limite:
    perfumaria((f'{cores["vermelho"]}Financiamento negado.{cores["limpa"]}'))
    print(f'O valor da casa de R$ {vcasa} em {meses} meses, ', end = '')
    print(f'o valor da prestação será de R$ {prestacao:.2f}')
    print(f'Seu limite é de R$ {limite:.2f}')
else:
    perfumaria((f'{cores["verde"]}Financiamento aprovado:{cores["limpa"]}'))
    print(f'O valor da casa de R$ {vcasa} em {meses} meses, ', end = '')
    print(f'o valor da prestação será de R$ {prestacao:.2f}')
    print(f'Seu limite é de R$ {limite:.2f}')