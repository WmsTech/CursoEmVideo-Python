num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))
print('Os numeros digitados foram {}, {} e {}.' .format(num1, num2, num3))
maior = num1
if (num2 > num1) and (num2 > num3):
    maior = num2
if (num3 > num1) and (num3 > num2):
    maior = num3

menor = num1
if (num2 < num1) and (num2 < num3):
    menor = num2
if (num3 < num1) and (num3 < num2):
    menor = num3

print('O menor numero digitado foi {} e o maior numero foi {}.' .format(menor, maior))
