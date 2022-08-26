def perfumaria(X):
    print('-='*20)
    print(X)
    print('-='*20)

perfumaria('Analisador de Triângulos')

s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))

#regra do triângulo: cada um dos lados deve ser menor que a soma dos outros dois
if (s1 < (s2 + s3)) and (s2 < (s1 + s3)) and (s3 < (s1 + s2)):
    print('É possível formar um triângulo:')
else:
    print('não é possível formar um triângulo:')

