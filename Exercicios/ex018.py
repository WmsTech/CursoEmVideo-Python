from math import sin, cos, tan, radians
angulo = float(input('Digite um agulo em graus: '))
# radians(angulo)  -> A função radians() converte um angulo de graus para radianos.
print('Para o angulo de {:.1f}° o seno ({:.1f}°) = {:.2f}, o cos ({:.1f}°) = {:.2f} e a tan ({:.1f}°) = {:.2f}' .format(angulo, angulo, sin(radians(angulo)), angulo, cos(radians(angulo)), angulo, tan(radians(angulo))))
