from time import sleep
print('-=-' * 30)
print(f'{"Tabuada de Numeros inteiros":^90}')
print('-=-' * 30)
tabuada = 0
while True:
    print('Digite Um numero inteiro e será mostrado a sua tabuada [Numero negativo finaliza o programa]')
    num = int(input('-> '))
    if num < 0:
        break
    else:
        print('*' * 20)
        print(f'Tabuada do Numero {num}')
        print('*' * 20)
        '''while tabuada <= 10: # MiNhA sOLUÇÃO
            print(f'{num} x {tabuada:2} = {num * tabuada} ')
            tabuada += 1
            sleep(0.25)
        tabuada = 1'''
        for c in range(0, 11): # SOLUÇÃO DO PROFESSOR
            print(f'{num} x {c:2} = {num * c} ')
            sleep(0.25)
print('[>>>> Fim de Programa <<<<]')

