import heapq

if __name__ == '__main__':
    # arr = list(map(int, input().split()))
    # k = int(input())
    
    arr = [1, 5, 10, 9, 7, 6, 8, 11]
    k = 3
    print("sorted   :", sorted(arr))
    
    print("unsorted :", arr)
    heapq.heapify(arr)
    print("heapify  :", arr)
    min_values = []
    min_val = -1
    for i in range(k):
        min_val = heapq.heappop(arr)
        min_values.append(min_val)
        print("min val   :", min_val)
        print("after pop:", arr)
    print("min_values:", min_values)
    print(k, "th min value:", min_val)
