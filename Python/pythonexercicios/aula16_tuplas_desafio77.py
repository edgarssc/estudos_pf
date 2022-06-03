palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',)
vogais = ('a', 'e', 'i', 'o', 'u')
for cada in palavras:
    print("Na palavra ", cada, " temos", end=" ", sep="")
    for i in cada:
        if i in vogais:
            #imprime na mesma linha e depois pula uma linha
            print(i,  end=" ")
    print()

        

   
    