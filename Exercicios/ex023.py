numero = int(input('Digite um numero entre 0 a 9999: '))
und = numero // 1 % 10
dez = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10
print('Analisando...')
print('O numero {} possui {} Milhar(es), {} Centena(s), {} Dezena(s) e {} Unidade(s)' .format(numero, mil, cen, dez, und))