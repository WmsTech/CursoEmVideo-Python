from time import sleep
escolha = 4
fim = False
while escolha != 5: # Minha resolução
# while not fim: # Resolução do Professor
    if escolha == 4:
        print('Digite 2 numero.')
        n1 = float(input('-> '))
        n2 = float(input('-> '))
    print('''Os numeros informados foram {} e {}. Escolha uma Opção:
    1 - Somar Numeros
    2 - Multiplicar Numeros
    3 - Qual maior numero
    4 - Digitar Novos numeros
    5 - Sair do programa'''.format(n1, n2))
    escolha = int(input('-> '))
    if escolha == 1:
        print('{}'.format('*' * 50))
        print('{} -> {} + {} = {}'.format('Você escolheu Somar Numeros', n1, n2, n1 + n2))
        print('{}\n'.format('*' * 50))
    elif escolha == 2:
        print('{}'.format('*' * 55))
        print('Você escolheu Multiplicar Numeros -> {} X {} = {}'.format(n1, n2, n1 * n2))
        print('{}\n'.format('*' * 55))
    elif escolha == 3:
        if n1 > n2:
            print('{}'.format('*' * 80))
            print('Você escolheu saber qual o maior numero. Analisando {} e {}, {} é MAIOR.'.format(n1, n2, n1))
            print('{}\n'.format('*' * 80))
        elif n1 < n2:
            print('{}'.format('*' * 80))
            print('Você escolheu saber qual o maior numero. Analisando {} e {}, {} é MAIOR.'.format(n1, n2, n2))
            print('{}\n'.format('*' * 80))
        else:
            print('{}'.format('*' * 80))
            print('Você escolheu saber qual o maior numero. Analisando {} e {}, ambos são IGUAIS.'.format(n1, n2))
            print('{}\n'.format('*' * 80))
    elif escolha == 5:
        print('FINALIZANDO...')
        fim = True
    sleep(2)
print('>>> Fim de Programa. <<<')