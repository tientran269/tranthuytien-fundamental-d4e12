shopping_list = ['watch', 'bag', 'perfume', 'shoes', 'bikini']
while True:
    steps = ['C','R','U','D']
    for index1, value1 in enumerate(steps):
        print(index1+1, value1)
        value1 = input('What steps you want to do?')
        if value1 == 'C':
            name = 'heels'
            shopping_list.append(name)
            print(shopping_list)
        if value1 == 'R':
            print(shopping_list)
        if value1 == 'U':
            for index, value in enumerate(shopping_list):
                print(index+1, value)
                old_value = input('Enter the item you want to edit')
                value = input('new value')
                index = shopping_list.index(old_value)
                shopping_list[index] = value
                for index, value in enumerate(shopping_list):
                    print(index+1, value)
        if value1 == 'D':
            value2 = input('Enter the item you want to delete')
            index = shopping_list.index(value2)
            deleted_item = shopping_list.pop(index)
            print(shopping_list)