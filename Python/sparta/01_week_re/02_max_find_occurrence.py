def find_max_occurred_alphabet(string):
    alphabet_find_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_find_array[arr_index] += 1

    max_occurrence = 0
    max_index = 0
    for index in range(len(alphabet_find_array)):
        alphabet_occurrence = alphabet_find_array[index]
        if max_occurrence < alphabet_occurrence:
            max_occurrence = alphabet_occurrence
            max_index = index

    return chr(max_index + ord('a'))


result = find_max_occurred_alphabet
print("정답 = a 현재 풀이 값 =", result("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", result("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", result("best of best sparta"))