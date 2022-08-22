students = ["mohammad", "iman", "sara"]
midterm = [78, 80, 94]
final = [90, 88, 92]

# {"mohammad": 90, "iman": 88, "sara": 94}  # <--- we want to achieve this max(midterm, final) for each student

best_grade_1 = [max(student[0], student[1]) for student in zip(midterm, final)]
best_grade_2 = [max(pair) for pair in zip(midterm, final)]
print(best_grade_1)
print(best_grade_2)

# max score:
persons = {t[0]: max(t[1], t[2]) for t in zip(students, midterm, final)}
for person in persons.items():
    print(person)
    
zip_obj_max = zip(
    students,
    map(
        lambda pair: max(pair),
        zip(midterm, final))
)
for person in zip_obj_max:
    print(person)

zip_obj_average = zip(
    students,
    map(
        lambda pair: (pair[0] + pair[1]) / 2,
        zip(midterm, final)
    )
)

print(dict(zip_obj_average))
