def linear_search(numbers,find_the_number):
    for index,value in enumerate(numbers):
        if value == find_the_number:
            return index
    return -1

def binary_search(numbers,find_the_number):
    left = 0 
    right = len(numbers)-1 
    mid=0
    while left<=right:
        mid = (left+right)//2
        mid_number = numbers[mid]
        if mid_number == find_the_number:
            return mid
        if mid_number<find_the_number:
            left = mid+1
        else:
            right = mid-1
    return -1

def binary_search_recrusive(numbers,find_the_number,left_index,right_index):
    if right_index<left_index:
        return -1
    mid_index=(left_index+right_index)//2
    if mid_index>= len(numbers) or mid_index<=0:
        return -1
    mid_number = numbers[mid_index]
    if mid_number == find_the_number:
        return mid_index
    if mid_number<find_the_number:
        left_index=mid_index+1
    else:
        right_index=mid_index-1
    
    return binary_search_recrusive(numbers,find_the_number,left_index,right_index)

if __name__=='__main__':
    # numbers=[i for i in range(1,1001)]
    numbers = [12, 15, 17, 19, 21, 24, 45, 67]
    find_the_number = 45
    index = binary_search(numbers,find_the_number)
    print(f'Number found at: {index}')
    right_index=len(numbers)-1
    left_index=0
    
    index1 = binary_search_recrusive(numbers,find_the_number,left_index,right_index)
    print(f'Number found at: {index1}')
    print("")