def linear_search(array, size, num):
    for i in range(0, size):
        print(i)
        if array[i] == num:
            return i
    return -1


sorted_arr = [111, 112, 130, 140, 150]
num_to_be_found = 110

index = linear_search(sorted_arr, len(sorted_arr), num_to_be_found)
if index == -1:
    print("not found")
else:
    print("index is:", index)
