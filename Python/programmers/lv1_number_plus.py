# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.



# 1. 입력받은 숫자를 문자열로 -> 리스트로
# 2. 반복문을 이용해 배열에서 꺼내서 더해준다.
# 3. 더할 때는 숫자로 더하다.

def solution(n):
    sn = list(str(n))
    num = 0
    for i in range(len(sn)):
        num += int(sn[i])    
    
    return num

print(solution(123))