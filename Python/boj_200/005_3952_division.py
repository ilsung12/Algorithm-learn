# division

arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)

arr_p = set(arr)
print(len(arr_p))