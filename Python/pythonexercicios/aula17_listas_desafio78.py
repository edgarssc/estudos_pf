#armazena um lista com 5 valores
valores = list()

#imprime qual foi o maior e menor valor e suas posições
for cada_valor in range(0, 5):
    valores.append(int(input(f'Digite um valor: {cada_valor}: ')))
print(f'-'*30)
print(f'Você digitou os valores {valores}')
print(f'-'*30)
print(f'O maior valor foi {max(valores)} nas posições {valores.index(max(valores))}')
print(f'O menor valor foi {min(valores)} nas posições {valores.index(min(valores))}')