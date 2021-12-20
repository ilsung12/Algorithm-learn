# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 
# 예를 들어 18의 자릿수 합은 1+8=9이고, 
# 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 
# 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, 
# solution을 완성해주세요.

def solution(x):
    # 1 8 -> 1 + 8 = 9 -> 18 % 9 == 0
    # 1 2 -> 1 + 2 = 3 -> 12 % 3 == 0
    # 1 . 각 자리수를 분할한다.
    # 2.  각 자리수의 합을 한다.
    # 3. 입력받은 수로 나눈다.
    # 4. 입력받은 수가 0 이면 하샤드다. ( True )


# 자릿수의 합을 구하기 위해 str을 이용해서 x를 문자열로 바꿉니다. 
# 그리고 반복문을 이용해서 자릿수를 하나씩 뽑아내서 sum에다가 더해줍니다. 
# 결국 sum = 자릿수의 합
# 자릿수의 합이 x로 나누어 떨어지는 것을 판단하기 위해서 x%sum을 해줍니다.
# 나누어떨어지면(==0) return True, 아니면 나누어떨어지지 않으므로 return False


    sum = 0
    for i in str(x):
        sum += int(i)
        print(sum)
    if x % sum == 0:
        return True
    else:
        return False


print(solution(223))