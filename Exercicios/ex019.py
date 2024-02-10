import random
print('Sorteador de Nomes')
n1 = input('Digite um nome: ')
n2 = input('Digite um nome: ')
n3 = input('Digite um nome: ')
n4 = input('Digite um nome: ')
nomes = [n1, n2, n3, n4]
# print('O nome sorteado foi {}.' .format(nomes[random.randint(0, 3)])) -> Minha solução
print('O nome escolhido foi {}' .format(random.choice(nomes)))
