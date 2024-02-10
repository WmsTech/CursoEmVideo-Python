print('-' * 42)
print(f'{"Vogais":^40}')
print('-' * 42)
print(f'Digite 12 palavras para ser analisada suas vogais.')
palavras = (str(input('Digite a palavra: ').strip().upper()), str(input('Digite a palavra: ').strip().upper()),
            str(input('Digite a palavra: ').strip().upper()), str(input('Digite a palavra: ').strip().upper()),
            str(input('Digite a palavra: ').strip().upper()), str(input('Digite a palavra: ').strip().upper()),
            str(input('Digite a palavra: ').strip().upper()), str(input('Digite a palavra: ').strip().upper()),
            str(input('Digite a palavra: ').strip().upper()), str(input('Digite a palavra: ').strip().upper()),
            str(input('Digite a palavra: ').strip().upper()), str(input('Digite a palavra: ').strip().upper()))
for item in palavras:
    print(f'\nA palavra {item} tem as seguintes vogais ', end='')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(f'{letra} ', end='')
