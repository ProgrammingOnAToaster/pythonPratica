name_input = input('Digite seu nome: ')
idade_input = input('Digite sua idade:')

name = None
idade = None

try:
    if(name_input.isalpha()):
        name = name_input
    
    else:
        
    idade = int(idade_input)

except  Exception as e:
    print(e)


print(f'Hello, {name}!')
print(f"You're, {idade} years old!")