def binary_search(array, left, right, num):
    if right < left:
        return -1
    else:
        mid = (right + left) // 2
        if array[mid] == num:
            return mid
        elif array[mid] > num:
            return binary_search(array, left, mid - 1, num)
        else:
            return binary_search(array, mid + 1, right, num)


arr = [2, 3, 4, 10, 40]
x = 10

result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
