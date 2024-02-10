'''from random import randint # Programa que pensa sempre em um numero entre 0 e 10 
print('{}'.format('<>') * 45) # e conta a quantidade de tentativas, a cada palpite
print('{:^90}'.format('ADVINHE O NUMERO')) # ele pensa em um novo numero
print('{}'.format('<>') * 45)

print('Estou pensando em um numero inteiro entre 0 e 10, consegue advinhar?')
tentativas = palpite = 0
numrand = 1

while palpite != numrand:
    numrand = randint(0, 10)
    palpite = int(input('Diga o seu palpite -> '))
    tentativas += 1
    if palpite != numrand:
        print('\033[31mEu pensei em {}, seu palpite foi {}. Você errou, tente novamente!\n'.format(numrand, palpite))
        print('\033[mEstou pensando em um numero inteiro entre 0 e 10, consegue advinhar?')
if tentativas == 1:
    print('\033[32mUau, você acertou! Eu pensei em {} e seu palpite foi {}. Parabéns, você acertou em {} tentativas!'.format(numrand, palpite, tentativas).replace('tentativas', 'tentativa'))
else:
    print('\033[32mUau, você acertou! Eu pensei em {} e seu palpite foi {}. Parabéns, você acertou em {} tentativas!'.format(numrand, palpite, tentativas))
'''

'''from random import randint  # programa que pensa em um numero entre 0 e 10
print('{}'.format('<>') * 45) # diz se o palpite é está proximo do numero e
print('{:^90}'.format('ADVINHE O NUMERO')) # mostra a quantidade de tentativas
print('{}'.format('<>') * 45)

print('Estou pensando em um numero inteiro entre 0 e 10, consegue advinhar?')
tentativas = palpite = 0
numrand = randint(0, 10)
while palpite != numrand:
    palpite = int(input('\033[mDiga o seu palpite -> '))
    tentativas += 1
    if palpite < numrand:
        print('\033[31mMais, tente novamente!\n')
    elif palpite > numrand:
        print('\033[31mMenos, tente novamente!\n')

if tentativas == 1:
    print('\033[32mUau, você acertou! Eu pensei em {} e seu palpite foi {}. Parabéns, você acertou em {} tentativas!'.format(numrand, palpite, tentativas).replace('tentativas', 'tentativa'))
else:
    print('\033[32mUau, você acertou! Eu pensei em {} e seu palpite foi {}. Parabéns, você acertou em {} tentativas!'.format(numrand, palpite, tentativas))'''

from random import randint  # programa que pensa em um numero entre 0 e 10 =>RESOLUÇÃO PROFESSOR<=
print('{}'.format('<>') * 45) # diz se o palpite é está proximo do numero e
print('{:^90}'.format('ADVINHE O NUMERO')) # mostra a quantidade de tentativas
print('{}'.format('<>') * 45)

print('Estou pensando em um numero inteiro entre 0 e 10, consegue advinhar?')
tentativas = palpite = 0
numrand = randint(0, 10)
acertou = False
while not acertou:
    palpite = int(input('\033[mDiga o seu palpite -> '))
    tentativas += 1
    if palpite == numrand:
        acertou = True
    else:
        if palpite < numrand:
            print('\033[31mMais, tente novamente!\n')
        elif palpite > numrand:
            print('\033[31mMenos, tente novamente!\n')

if tentativas == 1:
    print('\033[32mUau, você acertou! Eu pensei em {} e seu palpite foi {}. Parabéns, você acertou em {} tentativas!'.format(numrand, palpite, tentativas).replace('tentativas', 'tentativa'))
else:
    print('\033[32mUau, você acertou! Eu pensei em {} e seu palpite foi {}. Parabéns, você acertou em {} tentativas!'.format(numrand, palpite, tentativas))

