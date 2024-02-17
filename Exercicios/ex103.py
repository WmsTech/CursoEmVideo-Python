def ficha(name, g=0):
    print(f'O jogador {name} fez {g} gol(s) no campeonato.')


nome = str(input('Digite o nome do Jogador: ')).strip().title()
if not nome.isalpha():
    nome = '<desconhecido>'
gols = str(input(f'Fez quantos gols? '))
if not gols.isnumeric():
    gols = 0
ficha(nome, gols)
