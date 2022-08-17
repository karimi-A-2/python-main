def calculator(n, m, li):
    new_list = []
    sum_val = 0
    for i in range(1, len(li) + 1):
        sum_val += li[i - 1]
        if i % m == 0:
            new_list.append(sum_val)
            sum_val = 0
    if n % m != 0:
        new_list.append(sum_val)
    
    final_sum = 0
    for i in range(len(new_list)):
        if i % 2 == 0:
            final_sum += new_list[i]
        else:
            final_sum -= new_list[i]
    
    return final_sum


# if __name__ == '__main__':
#     my_list = [1, 2, 3, 4, 5, 6, 7, 8]
#     m = 1
#     print(calculator(len(my_list), m, my_list))
