input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i
        
        for j in range(n - i): # 01234, 1234, 234, 34 순으로 검사 (ft.i + j)
            if array[i + j] < array[min_index]:
                min_index = i + j
        print('IJ',i + j, 'i',i, 'j',j,'MIN', min_index, 'arr', array,'array[i + j]',array[i + j], 'array[min_index]',array[min_index] ,'array[i]',array[i])
        array[i], array[min_index] = array[min_index], array[i]

    return array

# 버블 정렬하고 다른 건 바로 "최솟값"을 찾아 변경하는 것입니다.
# 따라서, min_index 라는 변수를 통해 각각의 인덱스들과 비교합니다.
# 그리고 내부의 반복문이 끝나면, 최소 값의 인덱스와 i의 값들을 교체해주면 됩니다!


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))