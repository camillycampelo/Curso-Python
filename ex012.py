#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco= float(input('Digite o valor do produto: R$'))
desconto= preco * 0.05
novo= preco - (preco * 5) / 100
print('O valor do desconto é {}'.format(desconto))
print('O valor do produto com desconto de 5% é R${:.2f}'.format(novo))
