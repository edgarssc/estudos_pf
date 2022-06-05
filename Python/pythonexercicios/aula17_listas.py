# Aula 17, utilizando listas [] !!

# Adiciona elementos a lista com:
    # variavel.append()
# Insere elementos em uma posição especifica com:
    # variavel.insert()
# Remove elementos da lista com:
    # del variavel()
    # variavel.pop()
    # variavel.remove()
# Ordenando elementos da lista com:
    # variavel.sort()
    # variavel.sort(reverse=True)
# Tamanho da lista:
    # len(variavel)
#Exmplos:
#valores = list(range(4,11))
num = [2,4,5,7,8,9,10,12,13,15,16,17,18,19,20]
num [4] = 6
num.append(8)
#insere o valor 1 na posição 0
num.insert(0,1)
num.sort()
print(num)
print(len(num))
num.pop()
print(num)
if 5 in num:
    print("5 está na lista e será removido")
    num.remove(5)
    print(num)

# valor = list()
# for cada_valor in range(0, 5):
#     valor.append(int(input("Digite um valor: ")))
# print(valor)

a = [1,2,3,4,5]
b = a #Dessa forma a e b ficam ligadas, alterando uma, altera a outra
c = [4,5,7,8]
d = c[:] #Dessa forma a e b não ficam ligadas, alterando uma, não altera a outra
b[2] = 8
d[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')
print(f'Lista D: {d}')

