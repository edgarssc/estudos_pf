produto = float(input("Qual o preço do produto? "))
print("O produto que custava R${:.2f}, com desconto de 5% vai custar R${:.2f}.".format(produto, produto - (produto * 0.05)))