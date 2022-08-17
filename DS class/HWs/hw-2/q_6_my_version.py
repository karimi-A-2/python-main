def binary_search(array, left, right, num):
    print("L:", left, "R:", right)
    if right < left:
        return -1
    else:
        mid = (right + left) // 2
        print("mid:", mid)
        if num == array[mid]:
            return mid
        elif num < array[mid]:
            return binary_search(array, left, mid - 1, num)
        else:  # num > array[mid]:
            return binary_search(array, mid + 1, right, num)


sorted_arr = [111, 112, 130, 140, 150]
num_to_be_found = 110

last_index = len(sorted_arr) - 1
first_index = 0

index = binary_search(sorted_arr, first_index, last_index, num_to_be_found)

if index == -1:
    print("not found")
else:
    print("index is:", index)
