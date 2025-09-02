# import sys

from collections import deque 

# sys.stdin = open('input.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find_start(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return (i, j)
            
def find_end(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                return (i, j)

def bfs(sr, sc):
    visited = [[-1] * (N) for _ in range(N)]
    q = deque()

    visited[sr][sc] = 0 
    q.append((sr, sc))

    while q:
        r, c = q.popleft()

        # 종료 조건 
        if r == er and c == ec:
            return visited[r][c] -1

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] != 1 and visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))

    return 0

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    # 시작 지점 찾아서 할당 
    sr, sc = find_start(arr)
    # print(sr, sc)

    # 종료 지점 찾아서 할당 
    er, ec = find_end(arr)
    # print(er, ec)

    # bfs 시작 
    result_min = bfs(sr, sc)

    print(f'#{t} {result_min}')
