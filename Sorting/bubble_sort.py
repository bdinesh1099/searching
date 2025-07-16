def bubble_sort(numbers):
    size = len(numbers)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if numbers[j]>numbers[j+1]:
                temp = numbers[j]
                numbers[j]=numbers[j+1]
                numbers[j+1]=temp
                swapped = True
        if swapped == False:
            break

if __name__ == '__main__':
    # numbers = [8,7,9,3,4,5]
    # numbers = [1,2,3]
    # bubble_sort(numbers)
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    bubble_sort(elements)
    # print(numbers)
    print(elements)