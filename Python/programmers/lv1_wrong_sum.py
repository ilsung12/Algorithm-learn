# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 
# 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 
# 각 단어의 짝수번째 알파벳은 대문자로, 
# 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, 
# solution을 완성하세요.

# def solution(s):
#     st = list(map(str,s.split()))
#     arr = []

#     for i in range(len(st)):
#         # print(st[i])
#         for j in range(len(st[i])):
#             if j % 2 == 0 or j == 0:
#                 s = st[i][j].upper()
#                 arr.append(s)   
#             else:
#                 s = st[i][j].lower()
#                 arr.append(s)   
#         arr.append(' ')

#         #print(arr[i], end=' ')
#     print('"' + ''.join(arr[:-1])+ '"')
        

def solution(s):
    strings = s.split(" ")
    answer = []

    for i in range(len(strings)):
        strings[i] = list(strings[i])
        for j in range(len(strings[i])):
            if j % 2 == 0 :
                answer.append(strings[i][j].upper())
            elif j % 2 == 1 :
                answer.append(strings[i][j].lower())
        answer.append(" ")
        
    return ''.join(answer[:-1])

print(solution('try hello world'))

# return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))