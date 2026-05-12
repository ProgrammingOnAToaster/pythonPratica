import sys
from math import sqrt

print("Este módulo se chama ", __name__)
print(*sys.path, sep='\n')

def raiz_quadrada(n):
    return sqrt(n)