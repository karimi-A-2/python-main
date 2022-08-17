if __name__ == '__main__':
    h1_x = [0 for i in range(10)]
    h2_x = [0 for i in range(10)]
    h3_x = [0 for i in range(10)]
    h4_x = [0 for i in range(10)]
    print(h1_x)
    for x in range(2021):
        h1_x[(x ** 2) % 10] += 1
        h2_x[(x ** 3) % 10] += 1
        h3_x[(11 * (x ** 2)) % 10] += 1
        h4_x[(12 * x) % 10] += 1
    
    
    def print_list(num_list):
        print("[", end="")
        for num in num_list:
            print(str(num).rjust(3), end=", ")
        print("]")
    
    
    print("h1(x) results: ", end="")
    print_list(h1_x)
    print("h2(x) results: ", end="")
    print_list(h2_x)
    print("h3(x) results: ", end="")
    print_list(h3_x)
    print("h3(x) results: ", end="")
    print_list(h3_x)
