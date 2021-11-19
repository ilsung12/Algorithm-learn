# factorial


def facto(n):
    if n == 0 :
        return 1
    print(n)
    return n * facto(n - 1)

print(facto(3))