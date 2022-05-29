'''cores = {'limpa':'\033[m',
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
         'roxo':'\033[1;45m'}'''

d = int((input('Qual a distância da sua viagem? Responda em KM!')))
txc = 0.5
txl = 0.45
if d <= 200:
    print('O valor cobrado será de R$ {:.2f}'.format(d*txc))
else:
    print('O valor cobrado será de R$ {:.2f}'.format(d*txl))