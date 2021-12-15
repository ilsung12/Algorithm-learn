# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 
# 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때, 
# 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, 
# solution을 완성해주세요.

def solution(phone_number):
    answer = ''
    s = [] 

    for i in range(len(phone_number)-4):     
        s.append('*')    
        
    s += phone_number[len(s):]
    

    answer = ''.join(s)
    return answer
    
    
print(solution("01033334444"))
print(solution("027778888"))




# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
# def hide_numbers(s):
#     return "*"*(len(s)-4) + s[-4:]

# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print("결과 : " + hide_numbers('01033334444'));