def listaAlunos (A, B, C):
    total = (A|B|C)
    return total

def totalAlunos (A,B,C):
    nomes = (A|B|C)
    total = len(nomes)
    return total

#lista os alunos que estão matriculados em mais de uma turma
def alunosComDesconto(A,B,C):
    total = (A&B) | (A&C) | (B&C)
    return total

ingles = {'Gabriel', 'Caio', 'Maria', 'Ana', 'Juliano', 'Flávia', 'Rubens','Bruna'}
espanhol = {'Caio', 'Artur', 'Beatriz', 'Carolina', 'Maria', 'Juliano', 'Bruna', 'Rui'}
frances = {'Pedro', 'Bruna', 'Paula', 'Tiago', 'Maria', 'Flávia', 'Rui', 'Carolina'}

totalDeAlunos = totalAlunos(ingles,frances,espanhol)
listaDeAlunos = listaAlunos(ingles,espanhol,frances)
alunosDesconto = alunosComDesconto(ingles,espanhol,frances)

print(f'Existem um total de {totalDeAlunos} alunos!')
print(f'Os alunos matriculados são: {listaDeAlunos}')
print(f'Alunos com desconto: {alunosDesconto}')
