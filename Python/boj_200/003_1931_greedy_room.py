# room = int(input())

# outTime = 0
# cnt = 0

# for i in range(room):
#     N, K = list(map(int, input().split()))

#     if N <= K and N > outTime :
#         outTime = K
#         cnt += 1

# print(cnt)

######################################

rooms = int(input())
time = []

for _ in range(rooms):
  start, end = map(int, input().split())
  time.append([start, end])

time = sorted(time, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
print('sorted_1', sorted(time, key=lambda a: a[0]))
time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순
print('sorted_2', sorted(time, key=lambda a: a[1]))
print('time', time)

outTime = 0 # 회의의 마지막 시간을 저장할 변수
conut = 0 # 회의 개수를 저장할 변수


for i, j in time:
    
  if i >= outTime: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    conut += 1
    outTime = j
    print('i, j', i, j)

print('cnt', conut)
