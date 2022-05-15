from posixpath import split
from random import shuffle


a1 = str(input("Primeiro aluno: "))
a2 = str(input("Segundo aluno: "))
a3 = str(input("Terceiro aluno: "))
a4 = str(input("Quarto aluno: "))
lista = [a1,a2,a3,a4]
escolha = shuffle(lista) #shuffle - embaralha a lista
print("A ordem de apresentação será: {}.".format(lista))