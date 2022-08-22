
notasAlunos = []

for i in range(int(input("Digite a quantidade de notas: "))):
    nomes = (str(input(f'Digite o nome do {i+1}º aluno: ')))
    notas = (float(input(f"Digite a nota do {i+1}º aluno: ")))
    notasAlunos.append([nomes,notas])
#notasAlunos.sort([x[i] for x in notasAlunos ])
print(notasAlunos)