def print_msg():
    first_disk = list(map(int, input().split()))
    second_disk = list(map(int, input().split()))
    for first in range(0, 5):
        for second in range(0, 5):
            tmp = 0
            for i in range(0, 3):
                tmp += ((first_disk[(first + i) % 5] + second_disk[(second + i) % 5]) % 10) * (10 ** (2 - i))
            if tmp % 6 == 0:
                print("Boro joloo :)", end="")
                return
    print("Gir oftadi :(", end="")


print_msg()
# 0 1 2 3 4
