import math

if __name__ == '__main__':
    values = [23, 57, 184, 367]
    for n in values:
        product = 1
        print(n)
        for i in range(n):
            product *= (366 - i) / 366
        print(product)
        print(1 - product)
    # print(math.sqrt(366))
