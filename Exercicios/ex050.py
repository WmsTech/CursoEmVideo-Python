from time import sleep
print('{}'.format('<>') * 45)
print('{:^90}'.format('Somatorio de Numeros Pares'))
print('{}'.format('<>') * 45)
print('Digite 6 numeros inteiros e irei mostrar a soma entre eles, porém irei considerar apenas numeros pares!')
sleep(3)
s = 0
for c in range(1, 7):
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0:
        s += n

print('O somatorio dos numeros é {}'.format(s))


