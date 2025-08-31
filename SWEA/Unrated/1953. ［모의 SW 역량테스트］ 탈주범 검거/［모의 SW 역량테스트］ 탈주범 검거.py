# 상하좌우 순으로 파이프가 갈 수 있는 위치 
pipes = [[0,0,0,0],[1,1,1,1],[1,1,0,0],[0,0,1,1],[1,0,0,1],[0,1,0,1],[0,1,1,0],[1,0,1,0]]

# 현재 파이프가 바라보는 방향의 반대 파이프의 갈 수 있는 방향 
oppposite_d = [1,0,3,2]

# 델타 값 
di, dj = [-1,1,0,0],[0,0,-1,1]

def bfs(start_i,start_j):
    # 큐는 선입선출 
    q = []
    # 방문 기록 리스트, 같은 배열 크기에 각 칸에 도달한 시간을 기록 
    v = [[0]*M for _ in range(N)]
    # 횟수 저장 변수 
    ans = 0

    # 우선 큐에 방문한 거 넣는다 
    q.append((start_i,start_j))
    # 들어가자마자 넣었으니까 1로 방문 기록 
    v[start_i][start_j]=1
    # 방문했으니까 횟수 1추가 
    ans += 1

    # 더이상 방문할 지점이 없을 때까지 반복
    while q:
        # 큐의 제일 앞의 것을 꺼내서 만약에 이미 도달 시간이 최대시간이면 반복을 끝낸다 
        ci,cj = q.pop(0) 
        if v[ci][cj]==L:
            return ans

        # 4방향, 범위내, 조건(현위치 - 이동할 위치 모두 파이프 있는경우)
        for dr in range(4):
            ni,nj = ci+di[dr], cj+dj[dr]
            # 터널의 값을 구해서 파이프에 매치(각 번호가 의미하는 방향), 그래서 그 방향이 열려있는지 확인하고 그게 1인지 확인 
            # and 터널의 새로운 칸의 값을 구해서 그 방향의 파이프가 나의쪽으로 열려있는지 확인(그게 1인지 확인)
            # 맞으면 새로운 칸을 append
            # visited에서는 현재 칸의 시간에 하나를 더해서 시간을 기록 
            # 다 하면 횟수 추가 
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and pipes[tunnels[ci][cj]][dr]==1 and pipes[tunnels[ni][nj]][oppposite_d[dr]]==1:
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1
                ans += 1
    # 다 돌아도 L까지 못가면 리턴 
    return ans 

T = int(input())
for t in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnels = [list(map(int, input().split())) for _ in range(N)]

    ans = bfs(R,C)
    print(f'#{t} {ans}')