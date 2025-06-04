#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
ant = n - 1
suc = n + 1
print('O antecessor desse número é {}, e o sucessor é {}'.format(ant, suc))
