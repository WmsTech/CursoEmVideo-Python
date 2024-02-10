from time import sleep
print('{}'.format('<>') * 45)
print('{:^90}'.format('SEQUENCIA DE FIBONACCI'))
print('{}'.format('<>') * 45)
# num = int(input('Digite um numero inteiro e lhe mostrarei a sua Sequencia de Fibonacci: '))
num = int(input('Digite um numero inteiro de termos que lhe mostrarei a sua Sequencia de Fibonacci: '))
fn = 0
fanterior1 = 0
fanterior2 = 0
termo = 0
validacao = False
print('Dado o Numero {} a sua sequencia de fibonacci é:'.format(num))
while termo < num: # termo < num, por que termo inicializa em 0
    if termo > 1:
            fn = fanterior1 + fanterior2
            print(' {} '.format(fn), end=' ')
            fanterior2 = fanterior1
            fanterior1 = fn
            termo += 1
            sleep(0.5)
                
    else:
        print(' {} '.format(fn), end=' ')
        fanterior1 = 1
        fn = fanterior1
        termo += 1
        sleep(0.5)





'''while not validacao: # Minha solução, Recebe um numero inteiro e mostra a sequencia de Fibonacci até esse numero
    if termo > 1:       # ou até o termo mais proximo a esse numero.
            fn = fanterior1 + fanterior2
            if fn > num:
                validacao = True
            else:
                print('{}'.format(fn), end=' ')
                fanterior2 = fanterior1
                fanterior1 = fn
                termo += 1
    else:
        print('{}'.format(fn), end=' ')
        fanterior1 = 1
        fn = fanterior1
        termo += 1'''
        