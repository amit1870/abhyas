# Insertion Sort : builds final sorted array one at a time by comparisons.
# Props : 
#     1 : less efficient on large list
#     2 : Efficient on quite small data sets
#     3 : Adaptive : efficient for data sets already sorted
#     4 : Stable   : does not change relative order of elements with equal keys
#     5 : in-place : only requires a constant amount O(1) of additional memory space
#     6 : Online   : can sort a list as it receives

# Learn :
#     1 : Each iteration produces a sorted sub array.
#     2 : So only selected elemented need to be matched against sorted sub array
#     3 : While matching it will be placed in final postion.
#     4 : Function call done with object reference. So sorted array need not to be returned.


def insertion_sort(array):
    for index in range(1, len(array)):
        selected = array[index]
        reverse  = index - 1

        while reverse >= 0 and selected < array[reverse]:
            array[reverse+1] = array[reverse]
            reverse = reverse - 1

        array[reverse+1] = selected


def mergesort_inplace(array, left_index, right_index):
    if left_index < right_index:
        mid_index = left_index + (right_index - left_index) // 2
        mergesort_inplace(array, left_index, mid_index)
        mergesort_inplace(array, mid_index + 1, right_index)
        merge_inplace(array, left_index, mid_index, right_index)


def merge_inplace(array, start_index, mid_index, last_index):
    # check if direct merge is already sorted
    if array[mid_index] <= array[mid_index+1]:
        return

    # two pointers to maintain start of both arrays to merge
    left_index = start_index
    right_index = mid_index + 1

    while left_index <= mid_index and right_index <= last_index:
        if array[left_index] <= array[right_index]:
            left_index += 1

        else:
            temp = array[right_index]
            index = right_index

            while index != left_index:
                array[index] = array[index-1]
                index -= 1

            array[left_index] = temp

            # update all pointers
            left_index += 1
            mid_index += 1
            right_index += 1



def mergesort(array):
    if len(array) > 1:

        mid_index = len(array) // 2

        left_array = array[:mid_index]
        right_array = array[mid_index:]

        mergesort(left_array)
        mergesort(right_array)

        left_index = right_index = array_index = 0

        while left_index < len(left_array) and right_index < len(right_array):
            if left_array[left_index] <= right_array[right_index]:
                array[array_index] = left_array[left_index]
                left_index += 1
            else:
                array[array_index] = right_array[right_index]
                right_index += 1

            array_index += 1

        # if either left_index or right_index is not reached to limit
        while left_index < len(left_array):
            array[array_index] = left_array[left_index]
            left_index += 1
            array_index += 1

        while right_index < len(right_array):
            array[array_index] = right_array[right_index]
            right_index += 1
            array_index += 1


def quicksort(array, left_index, right_index):
    if left_index < right_index:
        pivot_index = partition(array, left_index, right_index)
        quicksort(array, left_index, pivot_index-1)
        quicksort(array, pivot_index+1, right_index)


def partition(array, left_index, right_index):
    pivot_value = array[right_index]
    i = left_index - 1
    j = left_index
    for j in range(left_index, right_index):
        if array[j] < pivot_value:
            i = i + 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

    temp = array[i+1]
    array[i+1] = pivot_value
    array[right_index] = temp
    return i + 1


def main():
    array = [10,7,19,89,20]
    mergesort_inplace(array, 0, len(array) - 1)
    print(array)



if __name__ == '__main__':
    main()
