cores = {'fim': '\033[m','branco': '\033[30m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m', 'lilas': '\033[35m', 'magenta': '\033[36m', 'cinza': '\033[37m'}

print('{}'.format('<>') * 45)
print('{:^90}'.format('E.F.E.F.M.S. Terra Oca'))
print('{}'.format('<>') * 45)

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2
print('Com as notas {:.1f} e {:.1f} a media do aluno foi {:.1f}'.format(n1, n2, media))

if media < 5:
    print('Você não alcançou a media e está REPROVADO!')
elif 5 <= media <= 6.9:
    print('Você não alacançou a media e está de RECUPERAÇÃO!')
else:
    print('Parabéns! Você foi aprovado!')
