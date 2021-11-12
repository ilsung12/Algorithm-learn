# BOJ - 11047 - 동전

N, K = map(int, input().split())

coins = []

for n in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)


cnt = 0
for i in coins:
    if K == 0:
        break
    cnt += K // i
    K %= i

print(cnt)
