if __name__ == '__main__':
    hs = [[0 for i in range(10)] for k in range(4)]
    for x in range(2021):
        hs[0][(x ** 2) % 10] += 1
        hs[1][(x ** 3) % 10] += 1
        hs[2][(11 * (x ** 2)) % 10] += 1
        hs[3][(12 * x) % 10] += 1
    
    
    def print_list(num_list):
        print("[", end="")
        for num in num_list:
            print(str(num).rjust(3), end=", ")
        print("]")
    
    
    for i in range(4):
        print("h", (i + 1), "(x) results: ", end="")
        print_list(hs[i])
