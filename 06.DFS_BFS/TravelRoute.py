def solution(tickets):
    answer = []
    dict = {}

    for ticket in tickets:
        if ticket[0] not in dict.keys():
            dict[ticket[0]] = ticket[1]
        else:
            dict[ticket[0]] += ticket[1]



    print(dict)

    return answer


tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))