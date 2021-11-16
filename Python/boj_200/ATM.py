person = int(input())
time = list(map(int, input().split()))

time.sort()

ret = 0
cnt = 0

for i in time:
    cnt += i
    ret += cnt

print(ret)