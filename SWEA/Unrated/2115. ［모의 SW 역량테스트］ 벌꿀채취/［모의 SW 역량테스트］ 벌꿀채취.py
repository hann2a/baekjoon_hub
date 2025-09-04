# import sys
import itertools 

# sys.stdin = open('input.txt', 'r')

# 첫번째 칸을 받아서 그 칸 동안 최대인 꿀 채취하고, 이익 계산하는 함수 
def calculate_honey(i, j):

    # 리스트로 꿀통을 받는다 
    # now_max: 해당 칸에서 최댓값을 구하는 변수, 이게 이 함수의 반환값이다 
    now_honey = honey_bucket[i][j:j+M]
    now_max = 0 

    # count는 칸들중에 몇 개를 선택할지 결정하는 반복문의 변수이다 1부터 M까지 돈다 
    for count in range(M, 0, -1):
        
        # 꿀통과 그 중에 몇 개를 선택할지 조합을 반환하는 반복문이다 변수는 subset이다
        # subset은 now_honey에서 count개를 선택하여 만들어진 조합, 즉 리스트이다
        for subset in itertools.combinations(now_honey, count):

            # 만약 해당 조합을 다 더했을 때 C가 넘어가면 반복문을 종료하고 다음 조합으로 넘어간다 
            if sum(subset) > C:
                continue
            
            # profit은 해당 조합을 다 더해주는 임시 변수이다
            profit = 0 
            for honey in subset:
                profit += honey ** 2

            # 만약 profit을 다 계산했는데 now_max보다 크다면 갱신한다
            if profit > now_max:
                now_max = profit 

    return now_max

T = int(input())
for t in range(1, T+1):
    N, M, C = map(int, input().split())
    honey_bucket = [list(map(int, input().split())) for _ in range(N)]

    # 최종 답 
    max_profit = 0 

    # 0부터 N-1 행까지, 0부터, N-M 열까지 도는 반복문 
    for i in range(N):
        for j in range(N-M+1):

            # i, j가 결정되면 해당 꿀통에서 도출할 수 있는 최댓값을 구한다 
            f_honey = calculate_honey(i, j)

            # i부터 N-1행까지, j+M 열부터 N-M 열까지 도는 반복문 (어차피 두 사람을 구분하지 않으므로 다음 행부터 시작해야 한다)
            for k in range(i, N):

                # k가 i면(두 사람이 같은 열에 있으면) j+M 열부터 돈다 
                if k == i:
                    for v in range(j+M, N-M+1):
                        s_honey = calculate_honey(k, v)
                        max_profit = max(max_profit, f_honey+s_honey)
                
                # k가 i가 아니면 0열부터 돈다 
                else:
                    for v in range(N-M+1):
                        s_honey = calculate_honey(k,v)
                        max_profit = max(max_profit, f_honey+s_honey)

                
                # -- k, v가 결정되면 두 번째 꿀통에 대한 최댓값을 구한다
                # 그 후에 max_profit과 그 둘을 더한 것을 비교해서 더 크다면 갱신한다

    print(f'#{t} {max_profit }')