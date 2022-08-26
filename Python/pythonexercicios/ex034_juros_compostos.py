def quizeporcento(X):
    X = X * 1.15
    return X

def dezporcento(X):
    X = X * 1.10
    return X

valor = float(input('Qual o seu salário: R$ '))

salPadrao = 1250
if valor > salPadrao:
    valor = quizeporcento(valor)
else:
    valor = dezporcento(valor)

print(f'Seu novo salário será: R$ {valor:.2f}')