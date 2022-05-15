from random import randint, random, choices
from secrets import choice
from time import sleep


cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print("\033[33m-=\033[m"*25)
print("\033[1;34mVou pensar num número entre 0 e 5. Tente adivinhar...\033[m")
print("\033[33m-=\033[m"*25)

# x = randint(1, 5) Poderia ter escrito assim, daí teria que retirar a linha do choice e ir direto para o if n == x
x = [0,1,2,3,4,5]
escolha = choice(x)
n = int(input(("Em que número eu pensei? ")))

print("\033[1;35mPROCESSANDO...\033[m")

sleep(2) #faz o computador agurar 2 segundos

if n == escolha:
    print("\033[1;033mParabéns, vc conseguiu me vencer!!!\033[m")
else:
    print("\033[1;31mNão foi esse número que pensei, vc perdeu.\033[m")
print("O número pensado foi {}.".format(escolha))