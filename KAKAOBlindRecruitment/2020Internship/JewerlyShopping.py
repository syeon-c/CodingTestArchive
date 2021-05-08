def solution(gems):
    answer = []
    shortestLen = len(gems) + 1
    start, end = 0, 0
    gemNum = len(set(gems))
    gems_dict = {}

    while end < len(gems):
        if gems[end] not in gems_dict:
            gems_dict[gems[end]] = 1
        else:
            gems_dict[gems[end]] += 1
        print(gems_dict)

        end += 1

        if len(gems_dict) == gemNum:
            while start < end:
                if gems_dict[gems[start]] > 1:
                    gems_dict[gems[start]] -= 1
                    start += 1
                    print(start)
                elif shortestLen > (end - start):
                    shortestLen = (end - start)
                    answer = [start + 1, end]
                    print(answer)
                    break
                else:
                    break

    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))