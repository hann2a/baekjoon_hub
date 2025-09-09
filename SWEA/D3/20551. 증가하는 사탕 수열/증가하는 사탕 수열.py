T = int(input())
for t in range(1, T+1):
    A, B, C = map(int, input().split())

    if A < 1 or B < 2 or C < 3:
        print(f'#{t} -1')
        continue

    eat_count = 0

    # B상자 = C상자 - 1 (B가 C보다 크거나 같을 때만)
    if B >= C:
        eat_count += B - (C-1)
        B = C - 1

    # A 상자 = B상자 - 1 (A가 B보다 크거나 같을 때만)
    if A >= B:
        eat_count += A - (B-1)
        A = B - 1

    print(f'#{t} {eat_count}')