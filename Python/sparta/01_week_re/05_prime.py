input = 20

prime_num = []
def find_prime_list_under_number(number):
    for n in range(2, number + 1):
        for i in prime_num:
            if n % i == 0 or i*i <= n:
                break
        else:
            prime_num.append(n)

    return prime_num

result = find_prime_list_under_number(input)
print(result)