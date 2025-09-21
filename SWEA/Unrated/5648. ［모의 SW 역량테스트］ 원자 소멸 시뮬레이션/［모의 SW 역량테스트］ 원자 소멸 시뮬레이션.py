# SWEA 5648 원자 소멸 시뮬레이션 

# 방향: 0=상, 1=하, 2=좌, 3=우  (y가 위로 증가)
dr = [0, 0, -1, 1]   # r 변화(좌/우)
dc = [1, -1, 0, 0]   # c 변화(상/하)

LIMIT = 2000  # 좌표 2배 스케일 기준 경계


def simulate(atoms):
    """
    atoms: {(r, c): (d, e)}  좌표는 2배 스케일.
    한 틱(0.5s)마다 동시에 이동  같은 칸 모이면 에너지 합산 후 소멸.
    """
    answer = 0
    cur = atoms

    while cur:
        acc = {}  # (nr, nc) -> [energy_sum, count, last_dir]

        # 1) 동시에 한 칸 이동
        for (r, c), (d, e) in cur.items():
            nr, nc = r + dr[d], c + dc[d]

            # 경계 밖은 소멸
            if nr < -LIMIT or nr > LIMIT or nc < -LIMIT or nc > LIMIT:
                continue

            key = (nr, nc)
            if key in acc:
                acc[key][0] += e
                acc[key][1] += 1
            else:
                acc[key] = [e, 1, d]

        # 2) 충돌 정산 + 다음 상태 구성
        nxt = {}
        for pos, (esum, cnt, d) in acc.items():
            if cnt > 1:        # 충돌  에너지 방출 후 소멸
                answer += esum
            else:              # 생존 다음으로 진행
                nxt[pos] = (d, esum)

        cur = nxt

    return answer


T = int(input().strip())
for tc in range(1, T + 1):
    N = int(input().strip())

    # 시작 좌표 중복 처리(즉시 폭발 케이스)
    base = {}  # (r, c)  [energy_sum, count, dir]
    for _ in range(N):
        r, c, d, e = map(int, input().split())
        key = (r * 2, c * 2)  # 0.5초 충돌 표현 위해 스케일 x2
        if key in base:
            base[key][0] += e
            base[key][1] += 1
        else:
            base[key] = [e, 1, d]

    atoms = {}
    answer = 0

    # 시작 위치에서 이미 겹친 원자 정산
    for pos, (esum, cnt, d) in base.items():
        if cnt > 1:
            answer += esum
        else:
            atoms[pos] = (d, esum)

    # 시뮬레이션 진행
    answer += simulate(atoms)

    print(f"#{tc} {answer}")
