#Módulos padrão do Python (import, from as e *)

#Boa prática
import math

def raiz_quadrada(n):
    return math.sqrt(n)



try:
    n = 0
    n_input = input("Enter with a number: ")
    n = int(n_input)

except (ValueError, TypeError) as e:
    print(f'Error! {e}')

print(raiz_quadrada(n))

#Boa Prática
#from math import sqrt

#from math import sqrt as raiz

#print(raiz(9))

#má pratica
#from math import *