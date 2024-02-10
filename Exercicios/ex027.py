nome = str(input('Digite o seu nome: ')).strip()
separado = nome.split()
print('Analisando o nome, o seu primeiro nome é {} e o ultimo sobrenome é {}' .format(separado[0], separado[len(separado) - 1]))