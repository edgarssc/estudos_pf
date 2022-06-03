produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
#mostra lista de produtos e seus respectivos preços
print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print('{:.<30}R$ {:.2f}'.format(produtos[pos], produtos[pos+1]))
print('-'*40)
