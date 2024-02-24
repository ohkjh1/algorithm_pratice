import sys
sys.stdin = open("input (2).txt", "r")

T=int(input())
for tc in range(1,T+1):
    N,K=map(int, input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    
    cnt=0
    result=0
    for i in range(N-K+1):
        for j in range(K):
            if arr[i][j]==1:
                cnt+=1
            if cnt==3:
                result+=1
                    
    for i in range(N-K+1):
        for j in range(K):
            if arr[j][i]==1:
                cnt+=1
            if cnt==3:
                result+=1
                    
                
     
    print(f"#{tc} {result}")