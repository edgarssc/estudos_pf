

#Gerar cinco numeros aleatorios entre 1 e 100
from random import randint
gera_aleatorio = [randint(1,100) for i in range(5)]
print(gera_aleatorio)
#imprime o maior e o menor numero
print("O maior número é {} e o menor é {}".format(max(gera_aleatorio), min(gera_aleatorio)))

