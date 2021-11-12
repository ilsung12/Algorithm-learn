# 더하기 || 곱하기

def find_max_plus_or_multiply(array):

    num = 0
    for i in array:
        if i <= 1 or num <= 1:
            num += i        
        else:
            num *= i

    return num
 

result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))