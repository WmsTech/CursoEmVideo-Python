from time import sleep


def linha():
    print('-=-' * 20)


def maior(* numeros):
    linha()
    print(f'Analisando os numeros informados...')
    print(f'Foram informado {len(numeros)} numeros sendo eles -> ', end='')
    m = 0
    for pos, num in enumerate(numeros):
        print(num, end=' ')
        if pos == 0:
            m = num
        else:
            if num > m:
                m = num
        sleep(0.5)
    print()
    print(f'O maior valor informado foi {m}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()