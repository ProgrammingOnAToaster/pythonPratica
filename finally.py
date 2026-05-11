#try, except, else e finally

try:
    print('ABRIR O ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU POR ZERO')

#TANTO ELSE QUANTO O FINALLY SAO EXECUTADOS MESMO COM EXCECAO

finally:
    print('FECHAR ARQUIVO')
