extenso = ('Zero','um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
continuar = ' '
while True:
    while True:  
        num = int(input('Digite um Numero ente 0 e 20: '))
        if 0 <= num <= 20:
            break
    print(f'Você digitou o numero {extenso[num]}')
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if continuar in 'Nn':
        break
    continuar = ' '
