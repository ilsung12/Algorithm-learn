top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    answer = [0] * len(heights)
    while heights:
        height = heights.pop() # 진행방향이 우측에서 좌측이기 때문에 pop
        for idx in range(len(heights) - 1, 0 , -1): # # 진행방향이 우측에서 좌측이기 때문에
            if heights[idx] > height: # value 보다 index 가 크다면
                answer[len(heights)] = idx + 1 # answer 의 인덱스에 인덱스 값을 넣는다. 
                                               # (이때 len(heights)인 이유는 pop 과정에서 길이가 줄어들기 때문)
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))