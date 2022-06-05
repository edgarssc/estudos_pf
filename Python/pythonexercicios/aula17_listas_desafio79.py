#cadastrar valores em uma lista
valores = list()
#caso o número já exista, não adiciona
while True:
    valor = (int(input("Digite um valor: ")))
    if valor in valores:
        print(f'Valor duplicado, não adicionado {valor}')
    else:
        valores.append(valor)
        print(f'Valor adicionado com sucesso: {valores}')
    continuar = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if continuar == 'N':
        break
print("-"*30)
print(f'Você digitou os valores {sorted(valores)}')
print("-"*30)
