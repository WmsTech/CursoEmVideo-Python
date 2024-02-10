print('Calculadora de aumento salarial')
print('Salarios superiore a R$ 1250,00 rejuste de 10%, iguais ou inferiores a R$ 1250,00 reajuste de 15%.')
sal = float(input('Digite o valor do Salario R$ '))
if (sal > 1250):
    print('Para o Salario de R$ {}, o salario tem um aumento para R$ {:.2f}.' .format(sal, (sal + (sal * 0.10))))
else:
    print('Para o Salario de R$ {}, o salario tem um aumento para R$ {:.2f}.' .format(sal, (sal + (sal * 0.15))))
