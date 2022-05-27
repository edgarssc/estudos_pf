
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

velocidade = int(input("{}Qual a velocidade atual do carro:{}".format(cores['amarelo'],cores['limpa'])))
taxa = 7
limite = 80
multa = (velocidade - limite)*taxa

if velocidade <= 40:
    print("{}Tenha um bom dia! Dirija com segurança!{}".format(cores['azul'],cores['limpa']))
elif (velocidade >40 and velocidade <=80):
    print("Você está proximo do limite de velociadade... tenha cuidado:")
else: 
    print("Você foi multado por exceder o limite de velocidade de {}km/h \nSua multa é de: R$ {:.2f}!".format(limite, multa))
print("Tenha um bom dia!")