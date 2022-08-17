
if __name__ == '__main__':
    arr = list(map(int, input().split()))
    prime = 13
    for element in arr:
        print(element, ":", element % prime)
"""
22 34 56 41 18 72 20
out: 3
"""
