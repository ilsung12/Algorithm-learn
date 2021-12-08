# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
# 단 0 <= a, b <= 2147483647, b는 0이 아니다

n, m = input().split()

sum = int(n) + int(m)
sub = int(n) - int(m)
mul = int(n) * int(m)
quo = int(n) // int(m)
rem = int(n) % int(m)
div = float(n) / float(m)


print(sum)
print(sub)
print(mul)
print(quo)
print(rem)
print(format(div, '.2f'))