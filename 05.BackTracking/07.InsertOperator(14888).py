import sys


def dfs(cnt, result, p, m, mul, div):
    global max_result, min_result
    # 입력된 모든 숫자 탐색하면 최댓값과 최솟값 반환
    if cnt == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    # op 리스트의 요소가 존재하면 대응하는 연산자 수행하고 값 1 감소
    if p:
        dfs(cnt + 1, result + nums[cnt], p - 1, m, mul, div)
    if m:
        dfs(cnt + 1, result - nums[cnt], p, m - 1, mul, div)
    if mul:
        dfs(cnt + 1, result * nums[cnt], p, m, mul - 1, div)
    # 만약 result 가 음수이면 양수로 바꾼 몫을 취한 뒤, 그 몫을 음수로 변경
    if div:
        dfs(cnt + 1, -(-result // nums[cnt]) if result < 0 else result // nums[cnt], p, m, mul, div - 1)


# n 은 수의 개수, nums 은 입력 받은 수의 리스트, op는 연산자 정보 리스트
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
# 연산결과의 최대값과 최소값 선언
max_result = -1 * sys.maxsize
min_result = sys.maxsize

# op 리스트의 인덱스 0-3 을 각각 p(더하기) m(빼기) mul(곱하기) div(나누기)와 대응
dfs(1, nums[0], op[0], op[1], op[2], op[3])

print(max_result)
print(min_result)
