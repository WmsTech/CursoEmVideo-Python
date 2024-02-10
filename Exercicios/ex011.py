print('Calculadora de Tinta - Rendimento de 1L por M2')
altura = float(input('Digite a altura(m) da parede a ser pintada: '))
largura = float(input('Digite a largura(m) da parede a ser pintada: '))
print('A area da parede é A = {} m2, com isso precisa-se de {:.1f} L de tinta para a pintura.' . format((altura * largura), ((altura * largura) / 2)))
