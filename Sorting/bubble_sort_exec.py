def bubble_sort(elements,key):
    size = len(elements)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j][key] > elements[j+1][key]:
                temp =elements[j][key] 
                elements[j][key] = elements[j+1][key]
                elements[j+1][key] = temp
                swapped = True
        if not swapped:
            break
        

if __name__ == '__main__':
    elements = [
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    ]
    bubble_sort(elements, key='transaction_amount')
    print(elements)
