mercado = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
           'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 
           'Canetas', 22.30, 'Livro', 34.90, 'Regua', 7.50, 'Apontador', 2.50)
print('-' * 42)
print(f'{"Lista de Preços":^40}')
print('-' * 42)
for item in range(0, len(mercado), 2): # Minha Resolução
    print(f'{mercado[item]:.<30} R$ {mercado[item + 1]:6.2f}')
print('-' * 42)


'''count = 0
while count <= 21:
    print(f'{mercado[count]:.<30} R$ {mercado[count + 1]:6.2f}')
    count += 2
print('-' * 42)
'''

'''for item in range(0, len(mercado)): # Resolução professor
    if item % 2 == 0:
        print(f'{mercado[item]:.<30}', end='')
    else:
        print(f'R${mercado[item]:>7.2f}')
print('-' * 42)'''