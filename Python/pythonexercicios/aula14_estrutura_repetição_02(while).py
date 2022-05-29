#exemplo 1
# c =1
# while c < 10:
#     print(c)
#     c += 1
# print("FIM")

#exemplo 2
# r = 'S'
# while r == 'S':
#     n = input("Digite um valor: ")
#     r = str(input("Deseja continuar [S/N]")).strip().upper()
# print("FIM")

#desafio 1
# sexo = input("Digite seu sexo: ex: [M] ou [F] ").strip().upper()
# while (sexo != 'M') and (sexo != 'F'):
#     print('Você digitou um valor invalido, digite M ou F:')
#     sexo = input("Digite se sexo: ex: [M] ou [F] ").strip().upper()
# if sexo == 'M':
#     print("Seu sexo é masulino")
# else:
#     print("Seu sexo é feminino")

#desafio 2
from random import randint, random, choices
from secrets import choice
from time import sleep


cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print("\033[33m-=\033[m"*25)
print("\033[1;34mVou pensar num número entre 0 e 9 Tente adivinhar...\033[m")
print("\033[33m-=\033[m"*25)

# x = randint(1, 5) Poderia ter escrito assim, daí teria que retirar a linha do choice e ir direto para o if n == x
x = [0,1,2,3,4,5,6,7,8,9]
escolha = choice(x)
chute = int(input(("Em que número eu pensei? ")))
palpite = 1
while chute != escolha:
    print("\033[1;35mPROCESSANDO...\033[m")
    sleep(1) #faz o computador agurar 1 segundos
    print("\033[1;31mNão foi esse número que pensei, vc perdeu.\033[m")    
    palpite += 1 
    chute = int(input(("Em que número eu pensei? ")))
    
print("\033[1;35mPROCESSANDO...\033[m")
sleep(1) #faz o computador agurar 1 segundos
print("\033[1;033mParabéns, vc conseguiu me vencer!!!\033[m")
sleep(1) #faz o computador agurar 1 segundos
print("O número pensado foi {}.".format(escolha))
print("Você precisou de {} palpites!".format(palpite))