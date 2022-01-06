# 자연수 n이 매개변수로 주어집니다. 
# n을 3진법 상에서 앞뒤로 뒤집은 후, 
# 이를 다시 10진법으로 표현한 수를 return 하도록 
# solution 함수를 완성해주세요.

def solution(n):
    answer = ''

    while n >= 1:
        n, rest = divmod(n, 3)
        answer += str(rest)

    answer = int(answer, 3)

    return answer

print(solution(125))

# 1) divmod() : 몫과 나머지를 같이 반환해주는 함수

# 2) int(x, base) : base 진법으로 구성된 str 형식의 수를 10진법으로 변환해 줌

#                     python의 int 함수는 진법 변환을 지원합니다.