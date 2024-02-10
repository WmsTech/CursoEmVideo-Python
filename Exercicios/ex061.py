from time import sleep
print('{}'.format('<>') * 45)
print('{:^90}'.format('Progressão Aritmetica'))
print('{}'.format('<>') * 45)
print('Informe dados e formarei um Progressão Aritmetica!')
a1 = float(input('Digite o primeiro termo a Progressão: '))
r = float(input('Digite a Razão entre os termos da Progressão: '))
termos = 0
pa = 0
continuar = ' '
validacao = False
while termos == 0:
    termos = int(input('Digite a quantidade de Termos da progressão: '))
    if termos > 0:
        if a1 % 1 == 0 and r % 1 == 0:
            print('Dado que o primeiro termo sendo {:.0f} e a razão {:.0f}, a Progressão Aritmerica formada é:'.format(a1, r))
            sleep(1)
            '''for c in range(1, termos + 1):
                pa = a1 + (c - 1) * r
                print(' {} '.format(pa), end=' -> ')
                sleep(1)'''
            cont = 1
            while cont <= termos:
                pa = a1 + (cont - 1) * r
                print('{:.0f}'.format(pa), end='')
                if cont < termos:
                    print('  ->  ', end='')
                sleep(1)
                cont += 1
                validacao = False
                if cont > termos:
                    while not validacao:
                        continuar = str(input('\nDeseja continuar mostrando termos? [S/N]: ')).strip()[0]
                        if continuar in 'SsNn':
                            if continuar in 'Ss':
                                n = int(input('Quantos termos a mais deseja ver? ->'))
                                if n > 0:
                                    termos += n
                                    validacao = True
                                else:
                                    validacao = True
                            else:
                                validacao = True
                        else:
                            print('>>>> Resposta Invalida! <<<<', end='')
        else:
            print('Dado que o primeiro termo sendo {} e a razão {}, a Progressão Aritmerica formada é:'.format(a1, r))
            sleep(1)
            '''for c in range(1, termos + 1):
                pa = a1 + (c - 1) * r
                print(' {} '.format(pa), end=' -> ')
                sleep(1)'''
            cont = 1
            while cont <= termos:
                pa = a1 + (cont - 1) * r
                print('{}'.format(pa), end='')
                if cont < termos:
                    print('  ->  ', end='')
                sleep(1)
                cont += 1
            validacao = False
            if cont > termos:
                while not validacao:
                    continuar = str(input('\nDeseja continuar mostrando termos? [S/N]: ')).strip()[0]
                    if continuar in 'SsNn':
                        if continuar in 'Ss':
                            n = int(input('Quantos termos a mais deseja ver? ->'))
                            if n > 0:
                                termos += n
                                validacao = True
                            else:
                                validacao = True
                        else:
                            validacao = True
                    else:
                        print('>>>> Resposta Invalida! <<<<', end='')
    else:
        print('Com essa quantidade de termos não é possivel formar um PA')
print('Foram apresentados {} termos da progressão!'.format(termos))
print('[>>>> FIM DO PROGRAMA <<<<]')
