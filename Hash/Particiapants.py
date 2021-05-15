def solution(participant, completion):
    dict = {}

    for p in participant:
        dict[p] = dict.get(p, 0) + 1

    for c in completion:
        if dict[c] == 1:
            del dict[c]
        else:
            dict[c] -= 1

    return list(dict)[0]


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))