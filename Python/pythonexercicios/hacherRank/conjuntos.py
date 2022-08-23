
A = {1,2,3,4,5,6}
B = {6,7,8,9,11,12,2}

#operação de união (A ∪ B)
print('A | B = ',A|B)
print('A.union(b) => ', A.union(B))
print()
#operação de interseção (A ∩ B)
print('A & B = ',A & B)
print('A.intersection(B) => ', A.intersection(B))
print()
#operação de interseção (A - B) e (B - A)
print('A - B = ',A - B)
print('A.diference(B) => ', A.difference(B))
print()
print('B - A = ',B - A)
print('A.diference(A) => ', B.difference(A))
print()
# Adiciona um elemento ao conjunto
A.add(30)
print(A)
print()
# Adiciona os elementos de uma sequência iterável
A.update([15, 20, 28, 33])
print(A)
print()
#Descarta um elemento do conjunto,
# Diferentemente do set.remove(), o discard não gera um erro
# se o elmento a ser removido não existir
A.discard(30)
print(A)
print()
# Verifica se os conjuntos são disjuntos, ou seja,
# se não possuem nenhum elemento em comum
print(A.isdisjoint(B))
# Verifica se o conjunto é subconjunto de outro
print(A.issubset(B))
# Verifica se o conjunto contém outro conjunto (superset)
print(A.issuperset(B))

