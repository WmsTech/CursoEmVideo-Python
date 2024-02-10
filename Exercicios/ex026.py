frase = str(input('Digite uma frase: ')).strip()
print('Analisando a Frase...')
print('A letra "A" aparece {} vezes na frase, aparecendo primeiro na posição {} e aparecendo por ultimo na posição {}.' .format(frase.lower().count('a'), (frase.lower().find('a') + 1), (frase.lower().rfind('a') + 1)))