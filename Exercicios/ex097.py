def escreva(msg):
    print(f'>>> Você digitou a seguinte mensagem <<<')
    tam = len(msg) + 4
    print('~' * tam)
    print(f'{msg:^{tam}}')
    print('~' * tam)


txt = str(input('Digite uma mensagem: ')).strip()
escreva(txt)
