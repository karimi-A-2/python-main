import numpy as np


def inverse(a: np.array) -> np.array:
    # return np.linalg.inv(a)
    pass


def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(float(int, input().split())))
    
    a = np.array(a)
    
    print(inverse(a))


if __name__ == "__main__":
    main()
