#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

#– Até 9 anos: MIRIM

#– Até 14 anos: INFANTIL

#– Até 19 anos: JÚNIOR

#– Até 25 anos: SÊNIOR

#– Acima de 25 anos: MASTER

from datetime import date

atual = date.today().year
anoNasc= int(input('Ano de Nascimento: '))
idade = atual - anoNasc

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Classificado: MIRIM')
elif idade <= 14:
    print('Classificado: INFANTIL')
elif idade <= 19:
    print('Classificado: JUNIOR')
elif idade <= 25:
    print('Classificado: SENIOR')
else:
    print('Classificado: MASTER')



