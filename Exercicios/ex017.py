from math import sqrt, pow, hypot
print('Calcualdora de hipotenusa.')
co = float(input('Digite o valor do cateto oposto em cm: '))
ca = float(input('Digite o valor do cateto adjacente em cm: '))
hipotenusa = hypot(co, ca)  # Calculo da hipotenusa usando a função -> math.hypot()
print('Dado o cateto oposto sendo {:.1f}cm e o cateto adjacente sendo {:.1f}cm, a hipotenusa vale {:.1f}cm.' .format(co, ca, (sqrt((pow(co, 2) + pow(ca, 2))))))
