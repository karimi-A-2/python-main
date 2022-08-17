if __name__ == '__main__':
    N = int(input())
    my_list = []
    for _ in range(N):
        str_list = input().split()
        # print(str_list)
        command_str = str_list[0]
        # print(command_str)
        if command_str == "insert":
            index = int(str_list[1])
            value = int(str_list[2])
            my_list.insert(index, value)
        elif command_str == "remove":
            index = int(str_list[1])
            my_list.remove(index)
        elif command_str == "append":
            value = int(str_list[1])
            my_list.append(value)
        elif command_str == "print":
            print(my_list)
        elif command_str == "sort":
            my_list.sort()
        elif command_str == "pop":
            my_list.pop()
        elif command_str == "reverse":
            my_list.reverse()

"""
7
insert 0 5
remove 6
append 9
print
sort
pop
reverse
"""
