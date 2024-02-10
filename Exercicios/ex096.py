"""def area(l, c):
    return l * c"""


def area(larg, comp):
    print(f'A area do terreno {larg} x {comp} é {larg * comp} m².')


largura = float(input('Digite a Largura (m): '))
comprimento = float(input('Digite o Comprimento (m): '))
'''a = area(largura, comprimento)
print(f'A area do terreno {largura} x {comprimento}(m) é {a} (m^2).')'''
area(largura, comprimento)