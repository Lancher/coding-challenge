

def num_of_1(n):
    res = 0
    while n:
        n &= n - 1
        res += 1
    return res


print(num_of_1(9))
