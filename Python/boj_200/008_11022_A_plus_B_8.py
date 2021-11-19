N = int(input())


for i in range(N):
    a, k = map(int, input().split())
    print('Case #%d: %d + %d = %d' %(i+1,a,k, a+k))
