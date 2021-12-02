input = 20


def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1

    return fibo_recursion(n - 1) + fibo_recursion(n - 2)


print(fibo_recursion(input))  # 6765

# 단점 :
# 방금 만들어본 함수에서 input 을 한 번 100으로 바꿔보세요!
# 그러면 실행했을 때 연산이 너~~무 오래걸려서 값이 나오질 않습니다.