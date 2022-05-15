from ast import Pow


n = int(input("Digite um valor: "))
print("O dobro de {} vale {}.".format(n, n*2))
print("O tripo de {} vale {}.".format(n, n*3))
print("A raiz quadrada de {} vale {:.2f}.".format(n, pow(n,(1/2))))