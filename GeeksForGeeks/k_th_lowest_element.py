def FirstKelements(arr, size, k):
    minHeap = []
    for i in range(k):
        minHeap.append(arr[i])
    print(minHeap)
    for i in range(k, size):
        minHeap.sort()
        print(minHeap)
        i_ = arr[i]
        print(i_)
        if minHeap[0] > i_:
            continue
        else:
            minHeap.pop(0)
            minHeap.append(i_)
        print(minHeap)
    print(minHeap)


arr = [11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45]
size = len(arr)
k = 3
FirstKelements(arr, size, k)
