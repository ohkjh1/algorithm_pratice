import sys; sys.stdin=open("input1.txt", "r")
t=int(input())

for tc in range(1,t+1):
    dr=[1,0,-1,0]
    dc=[0,1,0,-1]
    n,m = map(int,input().split())
    info=[list(map(int,input().split())) for _ in range(n)]

    max_val=0 # 모든 배열 하나하나 다 돌아가면서 비교한 후 
    #최종 결정되는 거 
    #중간에 바뀔 이유가 없으므로 전역변수로 
    for r in range(n):
        for c in range(m):
            me=info[r][c]

            for d in range(4): #r,c,nr,nc 다 인덱스 행렬값을 얻기 위한 인덱스 
                nr=r+dr[d]
                nc=c+dc[d]

                #n줄이니까  (행) // m개의 값=m개의 열
                if 0<=nr<n and 0<=nc<m:
                    me+=info[nr][nc]
            #하나씩 다 돌면서 최대값을 구해야 하니까 여기서 비교 
            if  me>max_val:
                max_val=me
    print(f"#{tc} {max_val}")
