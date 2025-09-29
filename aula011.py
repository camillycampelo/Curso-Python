nome= str (input('Qual é seu nome? '))
if nome == 'meninin':
    print("Que nome lindo!")
elif nome == 'Julin' or nome == 'Sergin' or nome == 'Paulin':
    print('Seu nome é muito fei!')
else:
    print('Gostei do seu nome.')
print('Bom dia, {}'.format(nome))
