total = maior = menor = 0
qtdNum = 0
resposta = 'S'
while resposta == 'S':
    n = int(input('Digite um numero: '))
    total += n
    qtdNum += 1
    if qtdNum == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    resposta = str(input('Deseja continuar infromando numeros? [S/N] ')).strip().upper()
print('Foram digitados {} numeros e a media deles é {}, sendo {} o maior e {} o menor.'.format(qtdNum, (total / qtdNum), maior, menor))
