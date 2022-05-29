from datetime import datetime


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

ano = int(input('Que ano quer analisar? '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print('O ano {} é {}BISSEXTO{}'.format(ano,cores['azul'],cores['limpa']))
else:
    print('O ano {} {}NÃO é BISSEXTO{}'.format(ano,cores['amarelo'],cores['limpa']))