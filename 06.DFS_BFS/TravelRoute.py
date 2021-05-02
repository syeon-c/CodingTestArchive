def solution(tickets):
    answer = []
    routes = {}

    for t in tickets:
        if t[0] not in routes.keys():
            routes[t[0]] = [t[1]]
        else:
            routes[t[0]] += [t[1]]

    print(routes)

    for k in routes.keys():
        routes[k].sort()

    print(routes)

    stack = ["ICN"]

    while stack:
        tmp = stack[-1]
        if tmp not in routes or len(routes[tmp]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp][0])
            routes[tmp] = routes[tmp][1:]
    print(answer)

    answer = answer[::-1]
    return answer


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution(tickets))
