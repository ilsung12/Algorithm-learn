# 자연수 n을 뒤집어 각 자리 숫자를 원소로 
# 가지는 배열 형태로 리턴해주세요.  
# 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

def solution(n):
    arr = list(str(n))
    s = []

    for i in range(1, len(arr) + 1):
        s.append(int(arr[-i])) # 끝에 인덱스 부터 넣기
             
    return s

print(solution(12345))

# 파이써닉
# def digit_reverse(n):
#    return list(map(int, reversed(str(n))))