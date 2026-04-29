#Generate a vect of names with first letter "a"
while True:
    try:
        quantity_names = int(input("Enter with number of names: "))

        vect = []

        for i in range(quantity_names):
            name = input("Enter with a name: ")
            if name[0] == 'A':
                vect.append(name)

        print('\n')
        print(f'names with A: ')
        for names in vect:
            print(names)
        
        break

    except ValueError:
        print("Error, please enter an integer number!")







