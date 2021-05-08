def swap_road(roads):
    for r in roads:
        r[0], r[1] = r[1], r[0]
    return roads


def search(i, end, roads, traps, visited, result):
    global answer
    if i == end:
        answer = min(answer, result)
        return

    if i in traps:
        if i not in visited:
            swap_road(roads)
            visited.append(i)

    for r in roads:
        if i == r[0]:
            print(i, r[1], result)
            print(roads)
            search(r[1], end, roads, traps, visited, result + r[2])


def solution(n, start, end, roads, traps):
    global answer
    answer = int(1e9)
    now = start
    visit_trap = []
    search(now, end, roads, traps, visit_trap, 0)

    return answer


n = 4
start, end = 1, 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]

print(solution(n, start, end, roads, traps))