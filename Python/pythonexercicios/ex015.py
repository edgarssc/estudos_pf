dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
custo_dia = 60 * dias
custo_km = 0.15 * km
total = float(custo_dia + custo_km)
print('O total a pagar é de R${:.2f}'.format(total))