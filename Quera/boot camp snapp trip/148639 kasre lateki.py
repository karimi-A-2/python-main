
def recursive(num, depth, n):
    if depth == n:
        return num
    else:
        return f'{num}+\\frac{{{recursive(2 * num, depth + 1, n)}}}{{{recursive(2 * num + 1, depth + 1, n)}}}'


n = int(input())
final_str = recursive(1, 1, n)
print(final_str)
