# 부모님을 기다리던 영일이는 검정/흰 색 바둑알을 바둑판에 꽉 채워 깔아 놓고 놀다가...

# "십(+)자 뒤집기를 해볼까?"하고 생각했다.

# 십자 뒤집기는
# 그 위치에 있는 모든 가로줄 돌의 색을 반대(1->0, 0->1)로 바꾼 후, 
# 다시 그 위치에 있는 모든 세로줄 돌의 색을 반대로 바꾸는 것이다.
# 어떤 위치를 골라 집자 뒤집기를 하면, 그 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀐다.

# 바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
# n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

# ==>>>>> 문제이해: x축을 한번 다 뒤집게 되면 
#                  y축 기준 x축이 있던 자리는 반대값이 되어있게된다
#                  그러므로 해당 겹치는 자리만 다르게 된다.
#                   쉽게 생각하면 쉬운 문제다.


# 바둑판 만들고,
stone_list = [[0 for i in range(19)] for j in range(19)]

# 바둑판 상태 입력받고
for i in range(19):
    stone_list[i] = list(map(int, input().split()))
    
n = int(input()) # 십자(+)뒤집기 횟수

for j in range(n):
    x, y = map(int, input().split()) # 뒤집을 기준 좌표 (x, y)

    for k in range(len(stone_list)):
        
        # x 축 : 10 , y 축 : 모두
        if stone_list[x - 1][k] == 0:
            stone_list[x - 1][k] = 1
        else:
            stone_list[x - 1][k] = 0

        # x 축 : 모두 , y 축 : 10
        if stone_list[k][y - 1] == 0:
            stone_list[k][y - 1] = 1
        else:
            stone_list[k][y - 1] = 0

# 출력하기
for idx in range(len(stone_list)):
    print(' '.join(map(str,stone_list[idx])))


# p = []

# for i in range(20) :
#   p.append([])
#   for j in range(20) :
#     p[i].append(0)

# for i in range(19) :
#   a = input().split()
#   for j in range(19) :
#     p[i+1][j+1] = int(a[j])

# n = int(input())
# for i in range(n) :
#   x, y = map(int, input().split())
#   for j in range(1, 20) :
#     if p[j][y] == 0 :
#       p[j][y] = 1
#     else :
#       p[j][y] = 0

#     if p[x][j] == 0 :
#       p[x][j] = 1
#     else :
#       p[x][j] = 0

# for i in range(1, 20) :
#   for j in range(1, 20) :
#     print(p[i][j], end = ' ')
#   print()