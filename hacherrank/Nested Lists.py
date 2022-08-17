def min_index(students):
    lowest_index = 0
    for i in range(1, len(students)):
        if students[i][1] < students[lowest_index][1]:
            lowest_index = i
    return lowest_index


if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # students = [['Harry', 0.0],
    #             ['Hbrry', 0.0],
    #             ['Tina', 0.0],
    #             ['Akriti', 1.0],
    #             ['Akrti', 1.0],
    #             ['Harsh', 1.0]]
    lowest_index = min_index(students)
    lowest_value = students[lowest_index][1]
    new_students = []
    for student in students:
        if student[1] == lowest_value:
            continue
        new_students.append(student)
    
    second_lowest_index = min_index(new_students)
    second_lowest_value = new_students[second_lowest_index][1]
    second_students = []
    for student in new_students:
        if student[1] == second_lowest_value:
            second_students.append(student[0])
    sorted_students = sorted(second_students)
    for student in sorted_students:
        print(student)
