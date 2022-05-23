nome = str(input("What's your name: ")).strip().capitalize()
if nome == "Maria":
    print("Your name is so beautifull ! ! !")
elif nome == "Pedro" or nome == "João" or nome == "Paulo":
    print("You name is famous in Brasil.")
elif nome in "Ana Cláudia Jéssica Juliana":
    print("Your name is a short...")
else:
    print("Your name is commum.")
print("Have a nice day {}.".format(nome))