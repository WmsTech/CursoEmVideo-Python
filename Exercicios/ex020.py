import random
print('Sorteador de ordem de apresentação')
n1 = input('Digite um nome: ')
n2 = input('Digite um nome: ')
n3 = input('Digite um nome: ')
n4 = input('Digite um nome: ')
nomes = [n1, n2, n3, n4]
nomes = random.sample(nomes, 4)
print('A ordem de apresentação dos trabalhos será:')
print('{} - {}' .format(1, nomes[0]))
print('{} - {}' .format(2, nomes[1]))
print('{} - {}' .format(3, nomes[2]))
print('{} - {}' .format(4, nomes[3]))
