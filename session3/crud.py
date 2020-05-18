while True:
    choices = input('what do you want to do? (c r u d)')
    stores = ['ca sau', 'khung long', 'phi thuyen']
    if choices == 'c':
        new_item = input('what do you want to add?')
        stores.append(new_item)
        print(*stores)
    elif choices == 'r':
        print(*stores)
    elif choices == 'u':
        for index, value in enumerate(stores):
            print(index+1, value)
        update_index = int(input('Enter the position you want to make change'))
        update_value = input('Enter new value')
        stores[update_index-1] = update_value
        print(*stores)
    elif choices == 'd':
        for index, value in enumerate(stores):
            print(index+1, value)
        delete_index = int(input('Enter the position you want to delete'))
        stores.pop(delete_index-1)
        print(*stores)
    else:
        break