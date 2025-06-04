# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
tempC= float(input('Digite a temperatura de hoje: '))
tempF= ((9 * tempC)/5) + 32
print('A temperatura de {}ºC para Farenheit é {}ºF'.format(tempC, tempF))
