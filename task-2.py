def search_bi(arr, target):
    print('\nsearch: ', target)
    start = 0
    end = len(arr) - 1
    itter = 0

    while start <= end:
        itter += 1
        mid = (end + start) // 2
        if target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            return (itter, arr[mid])
    
    if end < 0:
        return itter, arr[0]
    elif start >= len(arr):
        return itter, None
    else:
        return itter, arr[mid] if arr[mid] > target else (arr[mid + 1] if mid + 1 < (len(arr) - 1) else None)

arr = [1.33, 2.33, 3.444, 5.33, 6.2222, 7.24223, 8.3211, 9]

print(search_bi(arr, 5.33))
print(search_bi(arr, 5.331))
print(search_bi(arr, 5))
print(search_bi(arr, 9))
print(search_bi(arr, 9.1))
print(search_bi(arr, 10))
print(search_bi(arr, 1))
print(search_bi(arr, 1.33))