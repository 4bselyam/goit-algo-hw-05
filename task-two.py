def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if low < len(arr):
        upper_bound = arr[low]
    else:
        upper_bound = None

    return (iterations, upper_bound)

sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5]
target_value = 3.0
result = binary_search(sorted_array, target_value)
print(result)
