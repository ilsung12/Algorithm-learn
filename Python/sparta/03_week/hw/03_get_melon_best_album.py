# 1. 속한 노래가 많이 재생된 장르를 먼저 수록한다.(단, 각 장르에 속한 노래의재생 수 총합은 모두 다르다.)
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록한다.

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def get_melon_best_album(genre_array, play_array):
    n = len(genre_array)
    genre_total_play_dict = {} # 
    genre_index_play_array_dict = {}
    for i in range(n):
        genre = genre_array[i] # 장르 value
        play = play_array[i] # 플레이 value
        if genre not in genre_total_play_dict: # genre_total_play_dict 가 비어있다면,
            genre_total_play_dict[genre] = play # 해당 키에 play를 담는다.
            genre_index_play_array_dict[genre] = [[i, play]] # [i, play] - 인덱스와 play 수 를 담는다.
        else:
            genre_total_play_dict[genre] += play # 해당 키에 play를 누적한다.
            genre_index_play_array_dict[genre].append([i, play]) # [i, play] - 각각의 인덱스와 play 수 를 담는다.
        print('*************************************',i, '*********************************')
        print('genre의 value : ',genre)
        print('play의 value : ', play)
        print('genre_total_play_dict (play 수를 누적) : ', genre_total_play_dict)
        print('genre_index_play_array_dict (해당 index와 value를 누적) : ', genre_index_play_array_dict)
        print('----------------------------------------------------------------------------')

    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
    result = []
    print('역정렬1 : sorted_genre_play_array : ', sorted_genre_play_array)
    print('----------------------------------------------------------------------------')
    for genre, _value in sorted_genre_play_array:
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('genre ->>', genre)
        print('_value ->>', _value)
        index_play_array = genre_index_play_array_dict[genre]
        print('genre_index_play_array_dict[genre] ->>', genre_index_play_array_dict[genre])
        sorted_by_play_and_index_play_index_array = sorted(index_play_array, key=lambda item: item[1], reverse=True)
        print('역정렬 2 : sorted_by_play_and_index_play_index_array', sorted_by_play_and_index_play_index_array)
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        for i in range(len(sorted_by_play_and_index_play_index_array)):
            if i > 1: # 문제의 조건 : top 2 만 표출 (0 과 1)
                break
            result.append(sorted_by_play_and_index_play_index_array[i][0]) # i의 0번째 값 (key)을 배열로
            print('result : ', result)
    return result


print(get_melon_best_album(genres, plays))