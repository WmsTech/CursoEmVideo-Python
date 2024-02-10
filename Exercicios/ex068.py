from random import randint
print('-=-' * 30)
print(f'{"Par ou Impar":^90}')
print('-=-' * 30)
resposta = ' '
resultado = ' '
vitorias = 0
while True:
    num = int(input('Digite um valor: '))
    escolha = str(input('Escolha Par ou Ímpar [P/I]: ')).strip()[0]
    pc = randint(0, 10)
    if (num + pc) % 2 == 0:
        resposta = 'PAR'
        if escolha in 'Pp':
            resultado = 'Venceu'
            vitorias += 1
        else:
            resultado = 'Perdeu'
    else:
        resposta = 'ÍMPAR'
        if escolha in 'Ii':
            resultado = 'Venceu'
            vitorias += 1
        else:
            resultado = 'Perdeu'
    print('-' * 80)
    print(f'Você escolheu {num}, o computador escolheu {pc}. {num} mais {pc} dar {num + pc} que é {resposta}.')
    print('-' * 80)
    print(f'>>>>>  Você {resultado}! <<<<<')
    print('x - ' * 20)
    if resultado == 'Perdeu':
        break
print(f'Game over! Você foi um bom oponente, venceu {vitorias} vezes.')