N, K = map(int, input().split())

coin = []
for i in range(N):
    coin.append(int(input()))
coin.sort(reverse = True)


result = 0
for i in coin:
    if K == 0:
        break
    result += K//i
    K %= i
    
print(result)



