#desafio 1
while True:
    sexo = input("Digite se sexo: ex: [M] ou [F] ").strip().upper()
    if (sexo == 'M') or (sexo == 'F'):
        break
    else:
        print('Você digitou um valor invalido, digite M ou F:')
if sexo == 'M':
    print("Seu sexo é masulino")
else:
    print("Seu sexo é feminino")