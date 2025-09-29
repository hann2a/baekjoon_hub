"""
문제의 흐름 
제일 높은 곳에서 시작(최대 5개) > 낮으면 방문 가능, 1번만 K 이하로 깎을 수 있음 
갈 때까지 가봤을 때, 그 길이가 가장 긴 건? 
"""

# import sys
# sys.stdin = open('input.txt', 'r')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

"""
높은 걸 먼저 찾아보자 
N * N 배열을 모두 돌면서 highest를 갱신하고 해당 값을 리턴한다. 
"""
def find_top(arr):
    highest = 0 
    for i in range(N):
        for j in range(N):
            if arr[i][j] > highest:
                highest = arr[i][j]
    return highest

"""
시작 포인트와 chance 썼는지의 여부, 현재 길이를 갖고 돌아본다. 
도는 기준: 델타 탐색(상, 하, 좌, 우)
갈 수 있는 곳의 판단 여부: 배열을 벗어나지 않거나 방문하지 않음 < continue로 거름 
두 가지 경우의 수: 가려는 곳이 배열을 벗어나지도, 방문하지도 않았는데 
- top_point보다 낮다면 그냥 가면 됨 
- top_point보다 높다면 
    - 그리고 chance를 아직 소진하지 않았고, k만큼 깎았을 때 top_point보다 낮아진다면 
    - 백트래킹을 두 개 해야 됨 (깎지 않았을 때의 nr, nc와 visited )
length는 일단 시작할 때 1이고 dfs로 보낼 때마다 +1을 해줘서 길이를 잴 수 있음 
첫 번째 조건문에서 거르면서 그 전 max_result에서 최대 길이는 계속 갱신됨 
만약 r, c에서 가볼 수 있는 모든 길이를 다 가봤다면 호출한 dfs()들이 모두 닫히면서 함수가 종료됨 
tracking_map[i][j]로 돌고 있으므로 top_point와 같은 높이에서 모두 출발해볼 수 있게 됨 
이 모든 과정이 끝나고 들고 있는 max_result가 정답이 됨. 
"""
def dfs(r, c, chance, length):
    global max_result
    max_result = max(max_result, length)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        """
        방문했거나, 배열을 벗어나면 continue(다른 곳을 향함)
        """
        if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc]:
            continue 
        """
        if ) 만약 top_point가 새로운 지점보다 높다면 방문 가능
        """
        """
        elif ) 만약 chance가 존재하고 top_point보다 높은 새로운 지점에서 k를 제했을 때 top_point보다 작아진다면
        방문 가능 
        """
        if tracking_map[r][c] > tracking_map[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, chance, length+1)
            visited[nr][nc] = False
        
        elif chance and tracking_map[nr][nc] - K < tracking_map[r][c]:
            temporary = tracking_map[nr][nc]
            tracking_map[nr][nc] = tracking_map[r][c] - 1
            dfs(nr, nc, chance -1, length+1)
            visited[nr][nc] = False
            tracking_map[nr][nc] = temporary
        

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    tracking_map = [list(map(int, input().split())) for _ in range(N)]
    top_point = find_top(tracking_map)

    max_result = 0 
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if tracking_map[i][j] == top_point:
                """
                top_point가 여러개일 수 있으므로 백트래킹 
                top_point와 같은 높이인 곳이 시작점 
                """
                visited[i][j] = True
                dfs(i, j, 1, 1)
                visited[i][j] = 0 
    
    print(f'#{t} {max_result}')