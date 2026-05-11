#raise - lançando exceções(erros)
def nao_aceito_zero(d):
    if(d==0):
        raise ZeroDivisionError('Você está tentando dividir um número por zero!')
    return True

def deve_ser_int_ou_float(n):
    tipe_n = type(n)
    if not isinstance(n, (float, int)):
            raise TypeError(
                f'{n} deve ser int ou float.'
                f'"{tipe_n.__name__}" enviado.'
            )
    


def divide(n, d):


    nao_aceito_zero(d)
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    return n / d

print(divide(8, 'a'))    
