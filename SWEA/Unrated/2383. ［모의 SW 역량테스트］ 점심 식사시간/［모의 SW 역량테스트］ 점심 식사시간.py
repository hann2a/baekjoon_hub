import itertools
 
T = int(input())
 
import heapq

def calculate_stair_time(stair_time, arrivals):
    if not arrivals:
        return 0

    arrivals.sort()
    heap = []  # 현재 계단 위 3명의 '완료 시각'을 담는 최소힙

    for t in arrivals:
        # 자리가 꽉 차면, 가장 빨리 끝나는 사람의 완료시각까지 기다림
        if len(heap) == 3:
            earliest = heapq.heappop(heap)   # 가장 작은 완료시각
            start = max(t, earliest)
        else:
            start = t

        finish = start + stair_time
        heapq.heappush(heap, finish)

    # 마지막 완료시각 = 힙의 최대값
    return max(heap) if heap else 0


 
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    people = []  # 사람들의 위치
    stairs = []  # 계단의 위치 및 내려가는 시간
 
    # 입력 처리: 사람과 계단의 위치 저장
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                people.append((r, c))
            elif board[r][c] > 1:
                stairs.append((r, c, board[r][c]))  # (행, 열, 내려가는 시간)
 
    min_total_time = float('inf')
 
    # 모든 사람에 대해 계단 선택 경우의 수를 고려
    for stair_choice in itertools.product([0, 1], repeat=len(people)):
        first_stair_times = []  # 첫 번째 계단을 선택한 사람들의 도착 시간
        second_stair_times = []  # 두 번째 계단을 선택한 사람들의 도착 시간
 
        for i, (r, c) in enumerate(people):
            stair_idx = stair_choice[i]  # 이 사람이 선택한 계단 (0 또는 1)
            stair_r, stair_c, stair_t = stairs[stair_idx]
            arrival_time = abs(r - stair_r) + abs(c - stair_c) + 1  # 계단까지 이동 시간 +1분
            if stair_idx == 0:
                first_stair_times.append(arrival_time)
            else:
                second_stair_times.append(arrival_time)
 
        # 각 계단에서 최소 시간 계산
        first_time = calculate_stair_time(stairs[0][2], first_stair_times)
        second_time = calculate_stair_time(stairs[1][2], second_stair_times)
 
        # 두 계단을 이용하는 사람이 모두 내려가는 최소 시간 중 최댓값
        total_time = max(first_time, second_time)
        min_total_time = min(min_total_time, total_time)
 
    print(f"#{test_case} {min_total_time}")