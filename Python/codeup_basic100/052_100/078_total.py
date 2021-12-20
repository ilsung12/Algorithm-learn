# 영문 소문자 'q'가 입력될 때까지
# 입력한 문자를 계속 출력하는 프로그램을 작성해보자.


q = ''

while q != 'q': # 같지 않은 동안에
    q = str(input()) # 계속 입력받음
    print(q)
    if q == 'q': # break point
        break