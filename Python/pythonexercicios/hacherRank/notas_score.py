estudantes = [] 

for i in range(int(input('Digite o total de estudantes: '))):
    nomes = (str(input(f'Digite o nome do {i+1}º estudante: ')))
    notas = (float(input(f'Digite a nota do {i+1}º estudante: ')))
    estudantes.append([nomes,notas])

rankingNotas = sorted(list(set([x[1] for x in estudantes])))

#montando o ranking com as melhores notas
print(rankingNotas)    

#escolhendo a segunda nota
segundaMelhorNota = rankingNotas[1]

listaFinal = []
for i in estudantes:
    if segundaMelhorNota == i[1]:
        listaFinal.append(i[0])

for i in sorted(listaFinal):
    print(i)


#ordenadoNotas = [estudantes[i] for i in range(estudantes) if estudantes[i] == type(float)]