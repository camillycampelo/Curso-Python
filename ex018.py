#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
an= float(input('Digite o angulo que voce deseja: '))
seno= math.sin(math.radians(an))
cos= math.cos(math.radians(an))
tan= math.tan(math.radians(an))
print('O angulo de {:.2f} tem o seno de {:.2f}'.format(an, seno))
print('O cosseno é {:.2f}'.format(cos))
print('A tangente é {:.2f}'.format(tan))

