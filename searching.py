# search : linear and binary search

array = [10,20,39,49,89]
target = 49

def search(array, target):
    for index, item in enumerate(array):
        if item == target:
             return index
    else:
        return -1


def insertion_sort(array):
    for index in range(1, len(array)):
        selected = array[index]
        reverse  = index - 1

        while reverse >= 0 and selected < array[reverse]:
            array[reverse+1] = array[reverse]
            reverse = reverse - 1

        array[reverse+1] = selected

def binary_search(array, left_index, right_index, target):
    if left_index < right_index:
        
        mid_index = (left_index + right_index) // 2
        
        if array[mid_index] == target:
            return mid_index

        elif array[mid_index] > target:
            return binary_search(array, left_index, mid_index - 1, target)

        elif array[mid_index] <  target:
            return binary_search(array, mid_index + 1, right_index, target)

        else:
            return -1


insertion_sort(array)

print(binary_search(array, 0 , len(array) - 1, target))
