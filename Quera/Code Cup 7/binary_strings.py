# print(type(str(13)))

def flip_string(string, start_index, end_index): # included
    result_string = string[:start_index]

    
    changed_substring = ""
    for i in range(start_index, end_index + 1):
        changed_substring += str(1 - int(string[i]))

    result_string += changed_substring
    result_string += string[end_index + 1:]

    return result_string

# print(flip_string("01011100", 0, 7))

def make_list(n):
    output = []
    for i in range(n):
        output.append([])
    return output



def count_steps(olgoo, string):
    if olgoo == string:
        return 0
    flipped_string = string
    count = 0
    for i in range(len(string) - 1, -1, -1):
        if flipped_string[i] != olgoo[i]:
            flipped_string = flip_string(flipped_string, 0, i)
            count += 1
    return count



# number_of_testcases = int(input())
# strings_of_scenarios = make_list(number_of_testcases)

# for scenario in range(number_of_testcases):
#     test = input().split(" ")
#     number_of_strings = int(test[0])

#     for i in range(number_of_strings):
#         strings_of_scenarios[scenario].append(input())

# # print(strings_of_scenarios)

# steps_per_scenario = []
# for strings in strings_of_scenarios:
#     olgoo = strings[0]
#     counter = 0
#     for string in strings:
#         counter += count_steps(olgoo, string)
    
#     steps_per_scenario.append(counter)

# print(steps_per_scenario)


print(count_steps('01010', '01010')) # 2 + 3 + 2

        