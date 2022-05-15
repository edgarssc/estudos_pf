#x = range(10,7,-1)
#for n in x:
#    print(n)

from itertools import count
from re import S


s = "estou estudando"
print("how many times show the letter 'o'? {}".format(s.count("e")))
print("contagem de uma letra especifica dentro de um range, nesse caso a letra 'o': {}".format(s.count("o",0,10)))
print("What's the size of the sentence? {}".format(len(s)))#retorna o tamanho da string
print(s.find("estu")) #retorna o index de inicio da sequencia de letras procuras
if "estou" in s:
    print("existe a palvra buscada")
print(s.upper()) #deixa tudo maiúsculo
print(s.lower()) #deixa tudo minúsculo
print(s.capitalize()) #deixa o primeiro caracter maiúsculo
print(s.title()) #deixa em forma de título
print(s.strip()) #remove os espaços inúteis no início e no fim da frase
print(s.rstrip()) #remove apenas os últimos espaços da frase
print(s.lstrip()) #remove apenas os espaços no início da frase
print(s.split()) #gera uma nova lista com todas as palavras da cadeira de caracteres Ex: ["estou", "estudando", "agora"]
print('-'.join(s)) #adiciona um caractere "-" em cada letra