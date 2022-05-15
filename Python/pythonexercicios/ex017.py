from cmath import sqrt


co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comnprimento do cateto adjacente: "))
hp = sqrt((co ** 2) + (ca ** 2))
print("A hipotenusa vai medir {:.2f}.".format(hp))