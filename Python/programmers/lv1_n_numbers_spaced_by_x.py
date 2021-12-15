def solution(x, n):
    answer = []
    s = 0
    for _ in range(n):
        s += x
        answer.append(s)         

    return print(answer)

solution(2,5)
solution(4,3)
solution(-4,2)