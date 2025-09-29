# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual - ano

if idade < 18:
    saldo = 18 - idade
    print('Você tem {} anos.'.format(idade))
    anoAL = atual + saldo
    print('Seu alistamento será em {}.'.format(anoAL))
elif idade == 18:
    print('Você tem {} anos. Tem que se alistar imediatamente!'.format(idade))
elif idade > 18:
    saldo= idade - 18
    print('Você tem {} anos. Já deveria ter se alistado há {} anos.'.format(idade,saldo ))

