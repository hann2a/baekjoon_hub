T = int(input().strip())
for t in range(1, T+1):
    N, K = map(int, input().split())
    string = input().strip()            
    # 한 변의 길이 
    Long = N // 4                     

    numbers = set()

    for r in range(Long):
        # 4개의 변 시작점
        for j in range(4):
            start = (r + j * Long) % N
            # 인덱스가 넘치면 나눠서 붙인다 
            if start + Long <= N:
                part = string[start:start+Long]
            else:
                cut = (start + Long) % N
                part = string[start:] + string[:cut]
            numbers.add(int(part, 16))  
    # 내림차순 정렬 후 K번째
    arr = sorted(numbers, reverse=True)
    answer = arr[K-1]
    print(f"#{t} {answer}")