N, M, K = map(int, input().split())
add_arr = [list(map(int, input().split())) for _ in range(N)]
arr = [[5]*N for _ in range(N)]     

v = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):                
    i,j,age = map(int, input().split())
    v[i-1][j-1].append(age)         

for _ in range(K):  

    for i in range(N):
        for j in range(N):
            v[i][j].sort()                  
            for k in range(len(v[i][j])):  
                if v[i][j][k]<=arr[i][j]:   
                    arr[i][j]-=v[i][j][k]   
                    v[i][j][k]+=1          
                else:                       
                    while k<len(v[i][j]):   
                        arr[i][j]+=(v[i][j].pop()//2)
                    break

    
    for i in range(N):
        for j in range(N):
            for k in range(len(v[i][j])):   
                if v[i][j][k]%5==0:        
                    for di,dj in ((-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)):
                        ni, nj = i+di, j+dj
                        if 0<=ni<N and 0<=nj<N:
                            v[ni][nj].append(1)

  
    for i in range(N):
        for j in range(N):
            arr[i][j]+=add_arr[i][j]

ans = 0
for i in range(N):
    for j in range(N):
        ans+=len(v[i][j])
print(ans)