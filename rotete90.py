
# 규칙 찾기
# 회전 전의 열 번호와 회전 후의 행 번호는 일치
# 회전 후의 열은 N(테이블의 길이)-1 에서 회전 전의 행을 뺸 값과 같다.

#             [1]                               [(0,0)]
# [1,2,3] ->  [2]       [(0,0),(0,1),(0,2)] ->  [(0,1)]
#             [3]                               [(0,2)]


def rotate_90(arr):
    # 1. 변수 (테이블의 길이 즉, 열 의 끝자리 값)
    N = len(arr)
    # 1.1 
    rotate_arr = [[0] * N for a in range(N)] # for A in range(n) : n의 횟수 만큼 A를 반복  

    # 2. 반복 (i, j): 배열의 위치값
    for i in range(N):
        for j in range(N):
            # 3. 핵심 공식
            rotate_arr[j][N - 1 - i] = arr[i][j]

            # 4. 값 반환
    return rotate_arr

# rotate_arr[j][n - 1 - i] : 회전 후
#                arr[i][j] : 회전 전

# rotate_90 = [
#     [0, 0, 1]
#     [0, 0, 2]
#     [0, 0, 3]]
    
arr = [
    [1, 2, 3],
    [0, 0, 0],
    [0, 0, 0]]

arr = rotate_90(arr)


for z in arr:
    print(z)
