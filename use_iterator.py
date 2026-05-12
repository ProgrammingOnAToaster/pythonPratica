iterable = ['one', 'two', 'tree', 'four', 'five', 'six', 'seven']
iterator = iter(iterable)
try:
    while True:
        print(next(iterator))
    
except StopIteration:
    print("Error, The list is close!")