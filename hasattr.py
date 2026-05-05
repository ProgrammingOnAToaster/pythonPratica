#dir, hasattr e getattr em python

string = 'Vitor'
method = 'upper'

if hasattr(string, method):
    print(f'Exists {method}')
    print(getattr(string, method)())

else:
    print(f'Method {method} dont exists')
