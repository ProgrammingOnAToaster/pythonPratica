list = ['Vitória', 'Marcos', 'Ana']
list_2 = []

def truthy(valor):
    return 'truthy' if valor else 'falsy'

list3 = []

if truthy(list) != 'falsy':
    for item in list:
        list3.append(item)
else:
    print(f'Error, list values is:{truthy(list)}')

for item_rebind in list3:
    print(item_rebind)