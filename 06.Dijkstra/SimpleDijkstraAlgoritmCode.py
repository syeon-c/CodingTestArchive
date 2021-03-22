import sys
input = sys.stdin.readline
INF = sys.maxsize

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())

# 시작 노드 번호 입력
s = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for _ in range(n + 1)]

# 방문 여부를 체크해줄 목적의 리스트 생성
visited = [False] * (n + 1)

# 최단 거리 테이블 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력 받기
for _ in range(m):
    # a번 노드에서 b번 노드로 가는 비용이 c 라는 의미
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드의 번호 반환
def get_smallest_node():
    temp = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < temp and not visited[i]:
            temp = distance[i]
            index = i
    return index


def dijkstra(s):
    # 시작 노드에 대해서 초기화
    distance[s] = 0
    visited[s] = True
    for j in graph[s]:
        distance[j[0]] = j[1]

    # 시작 노드 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True

        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(s)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
    # 도달 할 수 없는 경우, 무한 출력
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])