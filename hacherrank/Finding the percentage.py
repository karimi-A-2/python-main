if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores_list = student_marks[query_name]
    # we also could use:
    # query_scores_list = student_marks.get(query_name)
    scores_sum = 0
    for i in query_scores_list:
        scores_sum += i
    query_scores_mean = scores_sum / 3
    # print(query_scores_mean)
    print("%.2f" % query_scores_mean)
"""
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
out: 56.00
"""
