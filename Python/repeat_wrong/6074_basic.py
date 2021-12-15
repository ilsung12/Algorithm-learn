# 영문 소문자(a ~ z) 1개가 입력되었을 때,
# a부터 그 문자까지의 알파벳을 순서대로 출력해보자.

# 영문자 1개가 입력된다.
# (a ~ z)

# a부터 입력한 문자까지 순서대로 공백을 두고 한 줄로 출력한다.

alpabet = str(input()) # str 으로 문자를 받는다.

# 받은 문자를 ord 메서드로 숫자(idx)로 변환하고,
# range메서드를 통해 1 부터 입력받은 글자까지 출력
for i in range(ord('a'), ord(alpabet) + 1):     
    print(chr(i), end=' ')

    
