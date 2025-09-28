import itertools
 
T = int(input())
 
def calculate_stair_time(stair_time, arrivals):
    if not arrivals:
        return 0

    arrivals.sort()
    in_use = []  # 현재 계단에 올라가 '내릴 때'의 완료시각들 (정렬 유지)

    for t in arrivals:
        # 도착한 시각 t 이전에 끝난 사람들 제거
        in_use = [x for x in in_use if x > t]

        if len(in_use) < 3:
            # 자리가 있음: 바로 시작
            finish = t + stair_time
        else:
            # 자리가 없음: 가장 빨리 끝나는 사람의 완료시각 이후에 시작
            earliest = in_use.pop(0)  # 정렬되어 있으니 앞이 최소
            finish = earliest + stair_time

        # 완료시각을 삽입 정렬로 넣어 정렬 유지
        import bisect
        bisect.insort(in_use, finish)

    return in_use[-1]  # 마지막 사람이 끝나는 시각

 
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