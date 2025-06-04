#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg= float(input('Largura da parede: '))
alt= float(input('Altura da parede: '))

area= larg * alt

print('Sua parede possui {} x {} de dimensão e sua área mede {}m²'.format(larg,alt,area))

tinta= area / 2

print('Para pintar essa parede, será necessário {}l de tinta'.format(tinta))
