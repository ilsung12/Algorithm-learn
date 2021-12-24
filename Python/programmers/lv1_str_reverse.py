# 문자열 s에 나타나는 문자를 큰 것부터 작은 순으로 정렬해 
# 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
# s는 영문 대소문자로만 구성되어 있으며, 
# 대문자는 소문자보다 작은 것으로 간주합니다.

def solution(s):
    arr =[]
    char = 0
    for i in range(len(s)):
        
       char = (ord(s[i]) - ord('a'))
       arr.append(chr(char + ord('a')))

    arr.sort(reverse=True)
    
    return ''.join(arr)

print(solution('Zbcdefg'))