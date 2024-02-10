a = float(input('Digite um tamanho em cm: '))
b = float(input('Digite um tamanho em cm: '))
c = float(input('Digite um tamanho em cm: '))
if (a < b + c) and (b < a + c) and (c < a + b):
    print('Com as medidas informadas é possivel fazer um triangulo.')
else:
    print('Com as medidas informadas não é possivel fazer um triangulo.')