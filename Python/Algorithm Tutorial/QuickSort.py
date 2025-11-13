def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [i for i in arr[1:] if i <= pivot]
        right = [i for i in arr[1:] if i > pivot]
        return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([1,5,199,15,123,151,34,31]))