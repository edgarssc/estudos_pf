from cmath import cos, sin, tan
from math import radians
#import os


valor = float(input("Digite o ângulo que vc deseja: "))
seno = sin(radians(valor))
coseno = cos(radians(valor))
tangente = tan(radians(valor))
print('O ângulo de {:.2f} tem o seno de {:.2f}'.format(valor, seno))
print("O ângulo de {:.2f} tem o seno de {:.2f}".format(valor, coseno))
print("O ângulo de {:.2f} tem o seno de {:.2f}".format(valor, tangente))
