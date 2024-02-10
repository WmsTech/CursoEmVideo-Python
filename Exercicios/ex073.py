print('{}'.format('<>') * 45)
print('{:^90}'.format('Brasileirão 2023'))
print('{}'.format('<>') * 45)
timesbr = ('Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Red Bull Bragantino', 'Fluminense', 'São Paulo',
           'Inter', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'Cruzeiro', 'Cuiabá', 'Santos', 'Bahia',
           'Corinthians', 'Goiás', 'Vasco', 'América-MG', 'Coritiba')
chapeoense = False
for pos, time in enumerate(timesbr):
    print(f'{pos + 1:2}° Colocado - {time}')
print('-' * 50)
print('Os 5 PRIMEIROS colocados na Tabela do Brasileirão 2023 são:')
print('-' * 50)
for count in range(0, 5):
    print(f'{count + 1}° colocado - {timesbr[count]}')
print('-' * 50)
print('Os 4 ULTIMOS colocados na Tabela do Brasileirão 2023 são:')
print('-' * 50)
print(timesbr[-4:])
'''for count in range(16, 21):
    print(f'{count + 1}° colocado - {timesbr[count]}')'''
print('-' * 50)
print('A tabela do Brasileirão em ordem alfabetica é: ')
print('-' * 50)
for pos, time in enumerate(sorted(timesbr)):
    print(f'{pos + 1:2}° - {time}')
print('-' * 50)
print('A Posição da Chapeoense é:')
print('-' * 50)
for pos, time in enumerate(timesbr):
    if time == 'Chapecoense':
        print(f'O time {time} está na posição {pos + 1}° da tabela')
        chapeoense = True
if not chapeoense:
    print('Chapecoense não está entre os 20 priomeiros colocados')