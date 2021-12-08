# 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.

S = list(map(int, input().split()))

for n in range(len(S)):
    if S[n] % 2 == 0:
        print("even")
    else:
        print("odd")