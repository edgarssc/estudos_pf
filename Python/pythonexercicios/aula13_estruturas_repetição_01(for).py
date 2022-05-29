from posixpath import split
from re import X
from time import sleep


# for i in range(10,0,-1):
#     print("passo {}".format(i))
#     sleep(1)
# print("Feliz ano novo!!!!!!")
# print(emoji.emojize("\U0001F387"*10))
# print("\n"*2)

# print("Todos os números pares que estão entre 1 e 50:")
# for i in range(1,51,1):
#     if (i %2) == 0:
#         print(i)

# print("Soma de todos os números que são multiplos de 3 e estão entre 1 e 500:")
# soma = 0
# for i in range(1,501):
#     if (i %3) == 0:
#         soma += i
# print(soma)

# print("Tabuada:")
# n = int(input("Digite um número entre 1 e 10:"))
# for i in range (1,10):
#     print("{} x {} = {}".format(n, i, n*i))

# print("Leia 6 números quaisquer e some apenas os números pares:")
# n = 0
# for i in range(1,7):
#     a = int(input("Digite o {}º número: ".format(i)))
#     if (a%2) == 0:
#         n += a
# print("A soma dos números pares digitados foi: {}".format(n))

print("Criando uma PA:")
p = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão dessa PA: "))
pa = 0
for i in range(1,11):
    pa += p + r
    print("{}º termo da PA é: {}".format(i,pa))
