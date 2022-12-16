import numpy as np


class MyLinAlgError(ValueError):
    pass


def print_m(m):
    for row in m:
        print(row)
    print()


def upper_triangle(m):
    for i in range(len(m)):
        candidate = i + 1
        while m[i][i] == 0 and candidate < len(m):
            (m[i], m[candidate]) = (m[candidate], m[i])
            candidate += 1
        top_row = m[i]
        for j in range(i + 1, len(m)):
            reduce_row = m[j]
            if top_row[i] != 0:
                reduce_factor = reduce_row[i] / top_row[i]
            else:
                reduce_factor = 0
            for k in range(i, len(reduce_row)):
                reduce_row[k] -= top_row[k] * reduce_factor
    return m


def row_echelon(m):
    for row in m:
        scale_factor = 0
        for k in range(len(row)):
            if row[k] != 0 and scale_factor == 0:
                scale_factor = row[k]
            if scale_factor != 0:
                row[k] /= scale_factor
    return m


def reduced_re(m):
    for i in reversed(range(len(m))):
        bottom_row = m[i]
        for j in reversed(range(i)):
            reduce_row = m[j]
            if bottom_row[i] != 0:
                reduce_factor = reduce_row[i] / bottom_row[i]
            else:
                reduce_factor = 0
            for k in range(i, len(reduce_row)):
                reduce_row[k] -= bottom_row[k] * reduce_factor
    return m


def check_non_singular(m):
    for i in range(len(m)):
        if m[i][i] == 0:
            raise MyLinAlgError("a is singular")


def solve_equation(a: np.array, b: np.array) -> np.array:
    if a.shape[0] != a.shape[1]:
        raise MyLinAlgError("a not square")
    if len(b) != a.shape[0]:
        raise MyLinAlgError("b dimension mismatch")
    b = np.vstack(b)
    m = np.concatenate((a, b), 1)
    m = m.tolist()
    
    m = upper_triangle(m)
    check_non_singular(m)
    m = row_echelon(m)
    m = reduced_re(m)
    
    m = np.array(m)
    return m[:, -1]


def inverse(a: np.array) -> np.array:
    if a.shape[0] != a.shape[1]:
        raise MyLinAlgError("a not square")
    n = a.shape[0]
    b = np.identity(a.shape[0])
    m = np.concatenate((a, b), 1)
    m = m.tolist()
    
    m = upper_triangle(m)
    check_non_singular(m)
    m = row_echelon(m)
    m = reduced_re(m)
    
    m = np.array(m)
    return m[:, n:]


def get_a_input():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(float, input().split())))
    a = np.array(a)
    return a


def get_b_input():
    b = list(map(float, input().split()))
    b = np.array(b)
    return b


def get_solve_sample():
    samples = [
        (
            np.array([
                [-3.0, 2.0, -6.0],
                [5.0, 7.0, -5.0],
                [1.0, 4.0, -2.0],
            ]),
            np.array([6.0, 6.0, 8.0])
        ),
        (
            np.array([
                [1.0, 1.0, 1.0],
                [1.0, -1.0, 2.0],
                [2.0, 0.0, 3.0],
            ]),
            np.array([3.0, 2.0, 1.0])
        ),
        (
            np.array([
                [1.0, 0.0, 0.0],
                [1.0, 0.0, 1.0],
                [0.0, 0.0, 1.0],
            ]),
            np.array([1.0, 4.0, 3.0])
        ),
        (
            np.array([
                [0.0, 0.0, 2.774193548387097],
                [0.0, 10.333333333333334, -15.0],
                [-3.0, 2.0, -6.0],
            ]),
            np.array([2.774193548387097, 16.0, 6.0])
        ),
    ]
    return samples[2]


def get_inv_sample():
    samples = [
        np.array([
            [1.0, 0.0, 2.0, 0.0],
            [1.0, 1.0, 0.0, 0.0],
            [1.0, 2.0, 0.0, 1.0],
            [1.0, 1.0, 1.0, 1.0],
        ]),
        np.array([
            [1, 4, 6],
            [4, 7, 7],
            [3, 3, 1],
        ]),
    ]
    return samples[0]


def main_solve():
    a, b = get_solve_sample()
    x = solve_equation(a, b)
    print(x)


def main_inverse():
    a = get_inv_sample()
    inv = inverse(a)
    print(inv)


if __name__ == "__main__":
    main_solve()
