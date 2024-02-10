total = cont = 0
while True:
    n = int(input('Digite um numero inteiro (999 para Parar): '))
    if n == 999:
        break
    else:
        total += n
        cont += 1
print(f'Foram digitados {cont} numeros e a soma entre eles é {total}.')
print(f'Foram digitados {"Teste":^20}')
