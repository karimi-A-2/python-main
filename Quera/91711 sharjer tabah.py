# todo: edit this and make it better
if __name__ == '__main__':
    n, x, y = map(int, input().split())
    num_list = list(map(int, input().split()))
    
    
    def delete_100():
        i = 0
        while i < len(num_list):
            if num_list[i] == 100:
                num_list.pop(i)
            else:
                i += 1
    
    
    delete_100()
    
    num_list.sort()
    # print(num_list)
    
    is_possible = False
    while True:
        if len(num_list) <= 1:
            is_possible = True
            break
        if sum(num_list) < 100 * (len(num_list) - 1):
            is_possible = False
            break
        if num_list[0] >= x:
            num_list[0] -= x
        elif num_list[1] >= x:
            num_list[1] -= x
            num_list.sort()
        else:
            is_possible = False
            break
        # print(num_list)
        
        num_list[-1] += y
        if num_list[-1] >= 100:
            num_list.pop()
        num_list.sort()
        # print(num_list)
    
    if is_possible:
        print('YES')
    else:
        print('NO')
