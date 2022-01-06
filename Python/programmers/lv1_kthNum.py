# 예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

# array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
# 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
# 2에서 나온 배열의 3번째 숫자는 5입니다.

# 0. commands = [2, 5, 3] 은 i = 2 부터 j = 5 까지 k = 3번째의 수 반환
# 1. 입력받은어레이의 인덱스

def solution(array, commands):

    arr=[]
    ans = []
    for ii in range(len(commands)):
        for _ in range(len(commands[ii])):
            i = commands[ii][0]
            j = commands[ii][1]
            k = commands[ii][2]


        arr.append(sorted(array[i-1:j]))
        ans.append(arr[ii][k-1])

    return ans



print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))