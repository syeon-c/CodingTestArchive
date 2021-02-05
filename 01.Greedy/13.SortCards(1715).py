import heapq

n = int(input())
heap = []
result = 0

for _ in range(n):
    heapq.heappush(heap, int(input()))

if n == 1:
    print(0)
    exit()

while len(heap) > 1:
    val = heapq.heappop(heap) + heapq.heappop(heap)
    result += val
    heapq.heappush(heap, val)

print(result)
