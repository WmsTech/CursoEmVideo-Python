sexo = ' '
'''while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu Sexo, Masculino (M) ou Feminino (F): ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Resposta Incorreta! Tente Novamente.\n')'''

while sexo not in 'MF':
    sexo = str(input('Digite seu Sexo, Masculino (M) ou Feminino (F): ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Resposta Incorreta! Tente Novamente.\n')
print('O sexo {} foi armazenadado com sucesso!'.format(sexo))

