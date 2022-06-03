#ler quatro valores e guardar em uma tupla
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
d = int(input("Digite o quarto valor: "))
tupla = (a, b, c, d)
#imprime quantas vezes o valor 9 apareceu na tupla
print("O valor 9 apareceu {} vezes".format(tupla.count(9)))
#imprime a primeira posição em que o valor 3 apareceu
print("O valor 3 apareceu pela primeira vez na posição {}".format(tupla.index(3)))
#imprime quais foram os numeros pares
for pos, cada in enumerate(tupla):
    if cada % 2 == 0:
        print("O número {} é par".format(cada))






