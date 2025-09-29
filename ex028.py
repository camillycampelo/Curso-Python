#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
pc = randint(0, 5)

print('='*15)
print('BEM VINDO!')
print('Tente adivinhar um número entre 0 e 5 e o PC tem que adivinhar.')
jogador =  int(input('Eu quero o número '))

if jogador == pc:
    print('PARABÉNS, VOCÊ VENCEU!')
else:
    print('IIIIH ERROU! O número era {}'.format(pc))

