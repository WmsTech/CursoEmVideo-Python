numeros = []
pos = 0
for n in range(0, 5):
    num = int(input('Digite um numero: '))
    if n == 0 or num > numeros[-1]:
        numeros.append(num)
    else:
        while pos < 5:
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                print(f'Numero adicionado na posição {pos}')
                break
            pos += 1
print(f'{numeros}')
    

'''print('-' * 50) # Minha resolução literalmente sem repetições
print(f'{"Ordenamento de Numeros":^50}')
print('-' * 50)
print('Digite 5 numeros que vou apresentá-los em ordem crescente')
numeros = []
pos = 0
# Com apenas um numero, ele é o maior e menor numero
num = int(input('Digite um numero: '))
n1 = n2 = n3 = n4 = n5 = num # n1, n2, n3, n4 e n5 serão os numeros organizado de ordem crescrente
print('Numero adicionado na lista...')

num = int(input('Digite um numero: '))
# Garantir que n1 seja o menor valor
if num >= n1:
    n2 = n3 = n4 = n5 = num
    pos = 1
else:
    n2 = n3 = n4 = n5 = n1
    n1 = num
    pos = 0
print(f'Numero adicionado na posição {pos}...')

num = int(input('Digite um numero: '))
if num >= n2: # equivalente a if num >= n1 and num >= n2
    n3 = n4 = n5 = num
    pos = 2
else:
    if num <= n1:
        n3 = n4 = n5 = n2
        n2 = n1
        n1 = num
        pos = 0
    else:
        n3 = n4 = n5 = n2
        n2 = num
        pos = 1
print(f'Numero adicionado na posição {pos}...')

num = int(input('Digite um numero: '))
if num >= n3: # equivalente a if num >= n1 and num >= n2 and num >= n3
    n4 = n5 = num
    pos = 3
else:
    if num <= n2:
        if num <= n1:
            n4 = n5 = n3
            n3 = n2
            n2 = n1
            n1 = num
            pos = 0
        else:
            n4 = n5 = n3
            n3 = n2
            n2 = num
            pos = 1
    else:
        n4 = n5 = n3
        n3 = num
        pos = 2
print(f'Numero adicionado na posição {pos}...')

num = int(input('Digite um numero: '))
if num >= n4: # equivalente a if num >= n1 and num >= n2 and num >= n3 and num >= n4
    n5 = num
    pos = 4
else:
    if num <= n3:
        if num <= n2:
            if num <= n1:
                n5 = n4
                n4 = n3
                n3 = n2
                n2 = n1
                n1 = num
                pos = 0
            else:
                n5 = n4
                n4 = n3
                n3 = n2
                n2 = num
                pos = 1
        else:
            n5 = n4
            n4 = n3
            n3 = num
            pos = 2
    else:
        n5 = n4
        n4 = num
        pos = 3
print(f'Numero adicionado na posição {pos}...')

numeros.append(n1)
numeros.append(n2)
numeros.append(n3)
numeros.append(n4)
numeros.append(n5)

print(f'O numeros digitados em ordem foram {numeros}')'''
            


'''A quem interessar, bisect.insort(lista, n) já insere n na lista de forma ordenada:
import bisect
numbers = []
for i in range(5):
    n = int(input('Type a number: '))
    bisect.insort(numbers, n)
    print(f'Number {n} included in position {numbers.index(n)}')
print(f'Numbers typed: numbers')'''


