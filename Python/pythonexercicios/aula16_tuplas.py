#Tuplas são imutáveis
lanche = ("suco", "hamburguer", "pizza", "batata frita")

#show index and value of variable
for pos, cada in enumerate(lanche):
    print("Eu vou comer {} na posição {}".format(cada, pos))
print("Estou cheio")