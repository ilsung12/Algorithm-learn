
# 1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되,
# 3의 배수인 경우는 출력하지 않도록 만들어보자.

# 예를 들면,
# 1 2 4 5 7 8 10 11 13 14 ...
# 와 같이 출력하는 것이다.

n = int(input())

sum = 0

for i in range(n):
    sum += 1
    if sum % 3 != 0:
        print(sum, end=' ')    
        
    if n <= sum:
        break
    