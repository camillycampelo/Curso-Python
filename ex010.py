# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Quanto de dinheiro voce tem?'))
dolar = real / 5.64

print('Com R${} voce pode comprar US${:.2f}'.format(real,dolar))
