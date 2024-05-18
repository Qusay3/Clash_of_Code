from typing import List

def insert_sort(arr: List[int]) -> List[int]:
    '''Sort an array of integers using insertion sort

    Args:
        arr (list[int]): an array of integers
    Returns:
        list[int]: the sorted array
    '''
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1

        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

    return arr

mylist = [4, 2, 7, 5, 9, 4, 5, 8, 1]
insert_sort(mylist)
print(mylist)
