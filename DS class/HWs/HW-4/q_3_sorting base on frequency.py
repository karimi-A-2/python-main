if __name__ == '__main__':
    arr = list(map(int, input().split()))
    values = []
    counts = []
    for element in arr:
        if element not in values:
            values.append(element)
            counts.append(1)
        else:
            counts[values.index(element)] += 1
    print("values:", values)
    print("counts:", counts)
    out = []
    while len(values) != 0:
        max_count_index = 0
        for i in range(1, len(counts)):
            if counts[i] > counts[max_count_index]:
                max_count_index = i
        value = values[max_count_index]
        count = counts[max_count_index]
        out += [value for k in range(count)]
        del values[max_count_index]
        del counts[max_count_index]
    
    print("sorted:", sorted(arr))
    print("   out:", out)
"""
8 9 8 5 6 1 9 8
out: [8, 8, 8, 9, 9, 5, 6, 1]
# arr = [8, 9, 8, 5, 6, 1, 9, 8]
# arr = [2, 5, 2, 8, 5, 6, 8, 8]
# arr = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
"""
