def binary_search(numbers,occuring_number):
    left_index=0
    right_index=len(numbers)-1
    while left_index<=right_index:
        mid_index=(left_index+right_index)//2
        mid_number= numbers[mid_index]
        if mid_number==occuring_number:
            return mid_index
        if mid_number<occuring_number:
            left_index=mid_index+1
        else:
            right_index=mid_index-1
    return -1

def find_all_occurences(numbers,occuring_number):
    index=binary_search(numbers,occuring_number)
    if index == -1:
        return []
    indices = []
    indices=[index]
    i=index-1
    while i>=0:
        if numbers[i]==occuring_number:
            indices.append(i)
        else:
            break
        i-=1
    i=index+1
    while i<=len(numbers):
        if numbers[i]==occuring_number:
            indices.append(i)
        else:
            break
        i+=1
    return indices    

if __name__=='__main__':
    # numbers=[i for i in range(1,1001)]
    numbers = [12, 15, 17, 19,21,21, 21, 24, 45, 67]
    occuring_number = 100
    indices =find_all_occurences(numbers,occuring_number)
    print(f'Number found at: {indices}')