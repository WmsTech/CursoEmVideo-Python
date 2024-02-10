print('-' * 50)
print(f'{"PARES E ÍMPARES":^50}')
print('-' * 50)
numeros = [[], []]

for c in range(0, 7):
    num = int(input(f'Digite o {c + 1}° numero: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
print(f'Dos numeros digitados, os numeros pares ordenados de forma crescente são {numeros[0]}')
numeros[1].sort()
print(f'Os ímpares ordenados de forma crescenrte são {numeros[1]}')
