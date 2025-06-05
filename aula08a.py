from math import ceil, sqrt
import random

#usando a biblioteca math
num= int(input('Digite um número'))
raiz= sqrt(num)
print('A raiz de {} é igual a {}'.format(num,ceil(raiz)))

#usando a biblioteca random
num= random.randint(1,10)
print(num)

