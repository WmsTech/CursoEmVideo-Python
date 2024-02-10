print('-=-' * 30)
print(f'{"Sistemas - Lojas Shopee":^90}')
print('-=-' * 30)
escolha = barato = ' '
total = caro = qtdProduto = valorbarato = 0
while True:
    nome = str(input('Digite o nome do produto: ')).strip().title()
    valor = float(input('Digite o valor do produto R$ '))
    qtdProduto += 1
    total += valor
    if qtdProduto == 1 or valor < valorbarato: # SOLUÇÃO DO PROFESSOR
        barato = nome
        valorbarato = valor
    '''if qtdProduto == 1: # MInHa solução
        barato = nome
        valorbarato = valor
    else:
        if valor < valorbarato:
            barato = nome
            valorbarato = valor'''

    if valor > 1000:
        caro += 1
    while True:
        escolha = str(input('Deseja continuar cadastrando produtos? [S/N] -> ')).strip()
        if escolha in 'SsNn':
            break
    if escolha in 'Nn':
        break
print(f'Foram cadastrados {qtdProduto} produtos. Foi gasto ao total R$ {total:.2f}, {caro} produtos custaram mais de R$ 1.000 e o nome do produto mais barato é {barato} que custa R$ {valorbarato:.2f}.')