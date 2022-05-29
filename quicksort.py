def quicksort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i < pivot]
    equal = [i for i in array[1:] if i == pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quicksort(less) + equal + [pivot] + quicksort(greater)


print(quicksort([10, 2, 3, 7, 12, 2, 5, 1, 3])) # => [1, 2, 2, 3, 3, 5, 7, 10, 12]

