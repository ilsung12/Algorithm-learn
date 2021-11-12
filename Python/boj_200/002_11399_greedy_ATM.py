# BOJ - 11399 - ATM

person = int(input())
time = list(map(int, input().split()))

time.sort()

ret = 0
# for i in range(person):
#     count = 0
#     for j in range(0, i + 1):
#         count += time[j]
#     ret += count

count = 0
for i in time:
    count += i
    ret += count


print(ret)
