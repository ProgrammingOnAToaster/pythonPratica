from modulo_m import raiz_quadrada

while True:
    try:
        n = int(input("Digite um número: "))
        print(f"A raiz quadrade de {n} é {raiz_quadrada(n)}")

        break

    except ValueError as e:
        print("Valor inválido!\n", e.__class__)
    
        
        continue
    