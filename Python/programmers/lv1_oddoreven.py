# 정수 num이 짝수일 경우 "Even"을 반환하고 
# 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

# def solution(num):
#     answer = ''
#     if num % 2 == 0:
#         answer = 'Even'
#     elif num == 0:
#         answer = 'Even'
#     else:
#         answer = 'Odd'
        
#     return answer

# print(solution(-3))


# 모범답안

def solution(num):
    
    if num % 2:
        return 'Odd'
    else:
        return 'Even'

print(solution(4))

# num%2가 0이 아닐 때만 True 이기 때문에 Odd가 되고 그 외에는 Even!!
# (num % 2 and 'Odd') or 'Even'
