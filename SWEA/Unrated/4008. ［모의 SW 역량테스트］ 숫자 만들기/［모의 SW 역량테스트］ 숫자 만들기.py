# import sys
# sys.stdin = open('input.txt', 'r')

def dfs(i, current):
    global max_val, min_val, operation, nums, N
    if i == N:
        if current > max_val: max_val = current
        if current < min_val: min_val = current
        return

    x = nums[i]

    if operation[0] > 0:   # +
        operation[0] -= 1
        dfs(i + 1, current + x)
        operation[0] += 1

    if operation[1] > 0:   # -
        operation[1] -= 1
        dfs(i + 1, current - x)
        operation[1] += 1

    if operation[2] > 0:   # *
        operation[2] -= 1
        dfs(i + 1, current * x)
        operation[2] += 1

    if operation[3] > 0 and x != 0:  # / (0쪽 절사)
        operation[3] -= 1
        dfs(i + 1, int(current / x))   # int()로 0쪽 절사
        operation[3] += 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    operation = list(map(int, input().split()))  # [+, -, *, /]
    nums = list(map(int, input().split()))
    max_val = -10**18
    min_val =  10**18

    dfs(1, nums[0])
    print(f"#{tc} {max_val - min_val}")