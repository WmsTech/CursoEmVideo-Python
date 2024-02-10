cidade = str(input('Digite o nome de uma cidade: ')).strip()
print('Procurando se a cidade começa com "SANTO"...')
print('Resposta -> {}' .format(cidade[:5].upper() == 'SANTO'))
      