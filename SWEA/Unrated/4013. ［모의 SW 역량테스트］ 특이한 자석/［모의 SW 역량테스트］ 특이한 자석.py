def dfs(num, dir, visited):
    # 방문 표시 
    visited[num] = 1
    # 오른쪽 이웃 검사 
    if num < 3:
        # 자성 다른 경우 
        if magnet[num][2] != magnet[num+1][6] and not visited[num+1]:
            dfs(num+1, -1*dir, visited)             
    # 왼쪽 이웃 검사 
    if num > 0:
        if magnet[num][6] != magnet[num-1][2] and not visited[num-1]:    
            dfs(num-1, -1*dir, visited)      

    if dir == 1:
        magnet[num] = [magnet[num].pop()] + magnet[num]
    else:
        magnet[num] = magnet[num][1:] + [magnet[num][0]]

T = int(input())
for t in range(1, T+1):
    K = int(input())
    magnet = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(K):
        num, dir = map(int, input().split())
        visited = [False] * 4  # visited 배열 초기화
        dfs(num-1, dir, visited)  # dfs 호출 시 visited를 인자로 넘기기

    result = 0
    for i in range(4):
        result += magnet[i][0] * 2 ** i
    print(f'#{t} {result}')
