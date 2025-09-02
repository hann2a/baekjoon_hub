# import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')

def bfs(start_node, V, adj_list):

    visited = [-1] * (V+1)
    q = deque()

    # 시작 노드 방문 처리 후 큐에 삽입 
    visited[start_node] = 0
    q.append(start_node)

    while q:
        curr_node = q.popleft()

        # 종료 조건 
        if curr_node == end:
            return visited[end]
        
        for next_node in sorted(adj_list[curr_node]):
            if visited[next_node] == -1:
                visited[next_node] = visited[curr_node] + 1
                q.append(next_node)
    
    return 0

T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())

    adj_list = [[] for _ in range(V+1)]
    for k in range(E):
        n1, n2 = map(int, input().split())
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)
    start, end = map(int, input().split())
    
    result_length = bfs(start, V, adj_list)

    print(f'#{t} {result_length}')