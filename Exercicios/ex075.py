numeros = (int(input('Digite um numero: ')), int(input('Digite um numero: ')),
           int(input('Digite um numero: ')), int(input('Digite um numero: ')))
print(f'Você digitou os seguintes numeros: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')

if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição.')
else:
    print(f'O numero 3 não está presente nos numeros informados.')

'''if numeros.count(3) == 0:  # Minha Resolução
    print(f'O numero 3 não está presente nos numeros informados.')
else:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição.')'''
print(f'Os numeros pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f'{n} ', end='')