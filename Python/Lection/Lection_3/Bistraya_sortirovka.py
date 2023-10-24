def quiq_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quiq_sort(less) + [pivot] + quiq_sort(greater)


print(quiq_sort([10, 5, 2]))