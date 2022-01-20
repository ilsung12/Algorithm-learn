# 문제 설명
# 주어진 숫자 중 3개의 수를 더했을 때 
# 소수가 되는 경우의 개수를 구하려고 합니다. 
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
# nums에 있는 숫자들 중 서로 다른 3개를 골라 
# 더했을 때 소수가 되는 경우의 개수를 
# return 하도록 solution 함수를 완성해주세요.

# 제한사항
# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 
# 중복된 숫자가 들어있지 않습니다.

from itertools import combinations
import math

# 소수 판별
def isprime(n):
	# 소수 판별할 숫자의 제곱근을 구한다.
    sqrt = math.sqrt(n)

	# 제곱근이 2보다 작으면 소수가 아니다.
    if sqrt < 2:
        return False

	# 2부터 제곱근까지 나눴을때 나머지가 0이 나오면 소수가 아니다.
    for i in range(2, int(sqrt+1)):
        if n % i == 0:
            return False
    
    return  True

def solution(nums):
    answer = 0
    # 중복을 제거한 3개로 된 숫자의 배열을 만듬
    arr = list(combinations(nums, 3))
	
    print('arr = > ',arr)
    # 3개의 배열을 소수판별 시킴 -> 세개의 합이 True 면
    for n1, n2, n3 in arr:
        print('n1 = > ', n1)
        print('n2 = > ', n2)
        print('n3 = > ', n3)
        print('----------')
        if isprime(n1+n2+n3):
            # answer를 + 1
            answer += 1

    return answer


print(solution([1,2,4,5]))