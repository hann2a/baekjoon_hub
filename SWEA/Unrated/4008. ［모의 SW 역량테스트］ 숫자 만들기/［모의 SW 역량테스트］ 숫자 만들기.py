def dfs(index, number, add, sub, mul, div):
    global min_result
    global max_result
    
    # 종료 조건 
    if index == N:
        if number < min_result:
            min_result = number
        if number > max_result:
            max_result = number
        return   # 종료 후 더 내려가지 않도록 return 필요

    if add:
        dfs(index+1, number+numbers[index], add-1, sub, mul, div)
    if sub:
        dfs(index+1, number-numbers[index], add, sub-1, mul, div)
    if mul:
        dfs(index+1, number*numbers[index], add, sub, mul-1, div)
    if div:
        dfs(index+1, int(number/numbers[index]), add, sub, mul, div-1)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    add, sub, mul, div = map(int, input().split())
    numbers = list(map(int, input().split()))
    
    min_result = int(1e8)
    max_result = int(-1e8)
    dfs(1, numbers[0], add, sub, mul, div)
    print(f'#{t} {max_result-min_result}')
