#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

viagem= int(input('Qual a distância da viagem? '))
if viagem <= 200:
    preco1 = viagem * 0.50
    print('O valor da sua passagem será R$ {:.2f}'.format(preco1))

else:
    preco2 = viagem * 0.45
    print ('O valor da sua passagem será R$ {:.2f}'.format(preco2))
