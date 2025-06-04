# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario= float(input('Digite o salário do funcionário: '))
aumento= salario * 0.15
novo= salario + aumento
print('O valor do aumento é {}'.format(aumento))
print('O salário de R${} com o aumento de 15% ficou R${} '.format(salario,novo))