# BOJ - 11047 - 동전

N, K = map(int, input().split())

coins = []

for n in range(N):
    coins.append(int(input()))
coins.sort(reverse=True) # 큰 값부터 K 에 나누어야 하기 때문 !

cnt = 0
for i in coins:
    if K == 0: # break Point
        break
    cnt += K // i # 몫이 카운트가 됨
    K %= i # 나머지 값을 K로 넣고 다시 돌림 

print(cnt)
