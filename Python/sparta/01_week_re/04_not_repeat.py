def find_not_repeating_first_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    not_repeat = []
    for index in range(len(alphabet_occurrence_array)):
        
        if alphabet_occurrence_array[index] == 1:
            not_repeat.append(chr(index + ord('a')))

            

    for char in string:
        if char in not_repeat:
            return char

    #return not_repeat
    return '_'


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))