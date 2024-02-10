from random import randint
from time import sleep
print('{}'.format('<>') * 45)
print('{:^90}'.format('Jokenpô'))
print('{}'.format('<>') * 45)
print('Eu sou o computador, vamos jogar Jokenpô?')
print('''Escolha Pedra, Papel ou Tesoura:
1 - Pedra
2 - Papel
3 - Tesoura''')
escolha = int(input('Sua escolha: ')) - 1
pc = randint(0, 2)
itens = ('Pedra', 'Papel', 'Tesoura')
print('JOKENPÔ!...')
sleep(2)

if escolha == 0:
    if pc == 0:
        print('Eu escolhi {}, Você escolheu {}, então temos um Empate, Vamos jogar novamente!'.format(itens[pc], itens[escolha]))
    elif pc == 1:
        print('Eu escolhi {}, Você escolheu {}, {} vence {}, Eu ganhei!'.format(itens[pc], itens[escolha], itens[pc], itens[escolha]))
    elif pc == 2:
        print('Eu escolhi {}, Você escolheu {}, {} vence {}, Você ganhou!'.format(itens[pc], itens[escolha], itens[escolha], itens[pc]))
elif escolha == 1:
    if pc == 0:
        print('Eu escolhi {}, Você escolheu {}, {} vence {}, Você ganhou!'.format(itens[pc], itens[escolha], itens[escolha], itens[pc]))
    elif pc == 1:
        print('Eu escolhi {}, Você escolheu {}, então temos um Empate, Vamos jogar novamente!'.format(itens[pc], itens[escolha]))
    elif pc == 2:
        print('Eu escolhi {}, Você escolheu {}, {} vence {}, Eu ganhei!'.format(itens[pc], itens[escolha], itens[pc], itens[escolha]))
elif escolha == 2:
    if pc == 0:
        print('Eu escolhi {}, Você escolheu {}, {} vence {}, Eu ganhei!'.format(itens[pc], itens[escolha], itens[pc], itens[escolha]))
    elif pc == 1:
        print('Eu escolhi {}, Você escolheu {}, {} vence {}, Você ganhou!'.format(itens[pc], itens[escolha], itens[escolha], itens[pc]))
    elif pc == 2:
        print('Eu escolhi {}, Você escolheu {}, então temos um Empate, Vamos jogar novamente!'.format(itens[pc], itens[escolha]))
else:
    print('Escolha invalida, tente novamente!')
        