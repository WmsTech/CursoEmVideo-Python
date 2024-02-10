from random import randint
from time import sleep
rand = randint(0, 5)
num = int(input('Estou pensando em um numero inteiro entre 0 e 5, qual numero estou pensando? '))
print('PROCESSANDO')
sleep(2)
if num == rand:
    print('Uau! Você acertou o numero que pensei!')
else:
    print('Não foi esse numero que pensei!')
print('Foi o numero que pensei' if num == rand else 'Resposta errada!')
