#Tuplas são imutáveis
# lanche = ("suco", "hamburguer", "pizza", "batata frita")

#show index and value of variable
# for pos, cada in enumerate(lanche):
#     print("Eu vou comer {} na posição {}".format(cada, pos))
# print("Estou cheio")

#Show values in order
# print(sorted(lanche))


# a =(1, 4, 6, 7, 3)
# b =(2 ,1, 3, 5, 7 , 8, 9)
# c = a + b
# print(c)
# #show number of times the value is repeted
# print(c.count(7))

# show the position is the value
# print(c.index(4))

#Desafio 1 da aula 16
#Cria uma variavel que armazena os valores de zero a vinte por extenso
extenço = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

# Armazena o valor digitado pelo usuario
numero = int(input("Digite um número entre 0 e 20: "))
while numero < 0 or numero > 20:
    print("Você digitou o número {} que não está no intervalo de 0 a 20".format(numero))
    numero = int(input("Digite um número entre 0 e 20: "))
for pos, cada in enumerate(extenço):
    if pos == numero:
        print("Você digitou o número '{}' que corresponde a '{}' por extenço".format(numero, cada))
        break
