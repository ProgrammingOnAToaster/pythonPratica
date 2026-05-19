import sys
from math import sqrt



from first_package.modulo_novo import soma_do_modulo

print("Este módulo se chama ", __name__)
print(*sys.path, sep='\n')

def raiz_quadrada(n):
    return sqrt(n)