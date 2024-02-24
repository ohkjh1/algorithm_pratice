t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split())
    info=[list(map(int,input().split())) for i in range(n)]


    dr=[0,1,0,-1]
    dc=[1,0,-1,0]

    ddia_r=[1,-1,-1,1]#[-1,1,1,-1]
    ddia_c=[1,1,-1,-1]#[1,1,-1,-1]

    a=[]

    max_value=0
    for i in range(n):
        for j in range(n):
            present=info[i][j]
            for k in range(1,m):#자기 포함 3번째까지 2를 더해야 함 eg)m=3 3번째 인덱스 2 
                for d in range(4):
                    nr=i+dr[d]*k
                    nc=i+dc[d]*k
                    if 0<=nr<n and 0<=nc<n:
                        present+=info[nr][nc]
            # if max_value < present:
            #     max_value= present
            a.append(present)
    
    for i in range(n):
        for j in range(n):
            present2=info[i][j]
            for k in range(1,m):
                for d in range(4):
                    nr=i+ddia_r[d]*k
                    nc=j+ddia_c[d]*k
                    if 0<=nr<n and 0<=nc<n:
                        present2+=info[nr][nc] 
            # if max_value < present2:
            #     max_value=present2
            a.append(present2)
    for i in a:
        if i >max_value:
            max_value=i

    print(f"#{tc} {max_value}")


    # max_value=[]

    # for i in range(n):
    #     for j in range(n):
    #         if info[i][j]:
    #             row=i
    #             col=j

    #         for k in range(1,m):
    #             nr=row+k
    #             nc=col+k
    #             if 0<nr<=n and 0<nc<=n :
    #                 info[i][j]+=info[nr][nc]

    #         max_value.append(info[i][j])

    
    # for i in range(1,n):
    #     for j in range(1,n):
    #         if i==j :
    #             info[i][j]+=info[i-1][j-1]
    #         if i==n-j-1:
    #             info[i][j]+=info[i-1][j-1]




