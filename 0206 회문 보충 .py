cnt=0
for i in range(N):
    for j in range(N-M+1):
        flag=1
        for  K in range(M//2):
            if a[i][j+K] != a[i][j+M-1-K]:
                flag=0
                break
        if flag:#0
            cnt+=1


def row_count(a):
    global cnt 
    for i in range(N):
        for j in range(N-M+1):
            flag = 1
            for k in range(M//2):
                if a[i][j+k] != a[i][j+M-1-k]:
                    flag=0
                    break
            if flag: cnt+=1
            


T=10
N=8
for tc in range(1,T+1):
    M=int(input())
    arr=[list(input()) for _ in range  (N)]
    ans=0
    row_count(arr)
    col_count(arr)
    print(f"#{tc} {ans}")
