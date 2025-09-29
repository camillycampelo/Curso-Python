#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cid= str(input('Digite o nome da sua cidade: ')).strip()
print('Analisando cidade...')
print(cid[0:5].upper() == 'SANTO')

