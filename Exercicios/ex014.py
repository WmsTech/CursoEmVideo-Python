print('Concersor de Temperatura')
t = float(input('Informe a temperatura em °C: '))
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F (Fahrenheit) e {:.1f}K (Kelvin)' . format(t, ((t * 1.8) + 32), (t + 373)))