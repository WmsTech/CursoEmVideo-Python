from math import factorial

print('{}'.format('<>') * 45)
print('{:^90}'.format('FATORIAL - WHILE'))
print('{}'.format('<>') * 45)

fatorial = 1
num = int(input('Digite um numero: '))
cont = num
print('O fatorial de {} é: \n{}! ='.format(num, num), end=' ')
while cont > 0:
    if num >= 2:
        print('{}'.format(cont), end='')
        print(' x ' if cont > 1 else ' = ', end='')    
    fatorial *= cont
    cont -= 1
print('{}.'.format(fatorial))

# -------------------------------------------------------
print('{}'.format('<>') * 45)
print('{:^90}'.format('FATORIAL - FUNÇÃO MATH'))
print('{}'.format('<>') * 45)
n  = int(input('Digite um numero: '))
contador = n
fact = factorial(n)
print('O fatorial de {} é: \n{}! ='.format(n, n), end=' ')
while contador > 0:
    if num >= 2:
        print('{}'.format(contador), end='')
        print(' x ' if contador > 1 else ' = ', end='')    
    contador -= 1
print('{}.'.format(fact))
# -------------------------------------------------------

print('{}'.format('<>') * 45)
print('{:^90}'.format('FATORIAL - FOR'))
print('{}'.format('<>') * 45)

n1 = int(input('Digite um numero: '))
f = 1
print('O fatorial de {} é: \n{}! ='.format(n1, n1), end=' ')
for c in range(n1, 0, -1):
    if n1 >= 2:
        print('{}'.format(c), end='')
        print(' x ' if c > 1 else ' = ', end='')
        f *= c
print('{}'.format(f))

