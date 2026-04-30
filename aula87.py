#isinstance - para saber se o objeto é de determinado tipo


list = [
    'Ana', 'Austin', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

names = []

for item in list:
    if isinstance(item, str) == True:
        names.append(item)


for name in names:
    print(name)