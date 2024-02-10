expressao = []
abrirParenteses = 0
fecharParenteses = 0
print('Digite uma expressão matematica entre parenteses obrigatoriamente.')
exp = str(input('Digite a expressão: ')).strip()
expressao.append(exp)
if '(' not in exp and ')' not in exp:
    print('A expressão não contém parenteses!')
else:
    '''for item in expressao:
        for letra in item:
            print(letra)'''
    for letra in expressao[0]:
        if letra == '(':
            abrirParenteses += 1
        if letra == ')' and abrirParenteses != fecharParenteses:
            fecharParenteses += 1
if abrirParenteses == fecharParenteses:
    print(f'Expressão Valida! Expressão digitada -> {expressao[0]}')
else:
    print(f'Expressão invalida!')