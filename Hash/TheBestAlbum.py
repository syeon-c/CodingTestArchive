from collections import defaultdict


def solution(genres, plays):
    answer = []
    genre_dict = {}
    total_list = {}

    for i in range(len(genres)):
        if genres[i] in genre_dict:
            genre_dict[genres[i]] += plays[i]
            total_list[genres[i]].append((plays[i], i))
        else:
            genre_dict[genres[i]] = plays[i]
            total_list[genres[i]] = [(plays[i], i)]

    genre_dict = sorted(genre_dict.items(), key = lambda x:x[1], reverse=True)

    print(genre_dict)
    print(total_list)
    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))