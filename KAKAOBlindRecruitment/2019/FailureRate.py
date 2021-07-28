def solution(N, stages):
    answer = []
    failure = {}
    user = len(stages)

    for i in range(N):
        if stages.count(i + 1) == 0:
            failure[i + 1] = 0
            continue

        failure[i + 1] = stages.count(i + 1) / user
        user -= stages.count(i + 1)

    failure = sorted(failure.items(), key=lambda item: item[1], reverse=True)

    for f in failure:
        answer.append(f[0])

    return answer


N = 5
stages = [2, 1, 2, 4, 2, 4, 3, 3]
print(solution(N, stages))
