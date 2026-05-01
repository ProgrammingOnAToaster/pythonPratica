#Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
#Mutáveis [] {} set()
#Imutáveis () "" 0 0.0 None False range(0, 10)

list = [0, 1, 2, 2, 3]
dict = {'Name':'Alan'}
set = set(list)
tuple = (list, dict, set)
string = ''
integer = 0
float = 0.0
null = None
false = False
interval = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'Teste', falsy('TESTE '))
print()
print(f'{list=}', falsy(list))
print(f'{dict=}', falsy(dict))
print(f'{set=}', falsy(set))
print(f'{tuple=}', falsy(tuple))
print(f'{string=}', falsy(string))
print(f'{integer=}', falsy(integer))
print(f'{float=}', falsy(float))
print(f'{null=}', falsy(null))
print(f'{false=}', falsy(false))
print(f'{interval=}', falsy(interval))