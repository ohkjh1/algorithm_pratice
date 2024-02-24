dr=[1,0,-1,0]
dc=[0,1,0,-1]


def maze_bfs(r,c):
    global ca
    q=[]
    visited=[[0]*N for _ in range(N)]
    q.append((r,c)) #q.append(maze[r][c]) 탐색 순서로 어떤 번호 노드 정점 번호라고 생각 즉 값을 넣으면 안됨 
    visited[r][c]=1


    while q: #q에 탐색순서에 따라 정점(노드) 넣고 
        #팝해서 charge(담당자)로 만들어서
        #주변의 것들도 q에 들어가도록 한다. 

        charge_r,charge_c=q.pop(0)#?
        if maze[charge_r][charge_c]==3:
            ca=visited[charge_r][charge_c]-2
            return ca 
        
        #팝한 charge(담당자)의 주변의 것을 탐색해서 q에 넣는 일 
        for d in range(4):
            nr=charge_r+dr[d]#nr=r+dr[d]#팝한 charge(담당자)의 주변의!!!!!
            nc=charge_c+dc[d]#nc=c+dc[d]#팝한 charge(담당자)의 주변의!!!!!

            if 0<=nr<N and 0<=nc<N and visited[nr][nc]==0 and maze[nr][nc]!=1:
                q.append((nr,nc))
                visited[nr][nc]=visited[charge_r][charge_c]+1 #여기서 계속 방문했다 표시로 1만 넣으려고 하는데, 
                #여기에는 우리가 도착 지점과 지점 간의 거리를 계산해야 하므로 계속 이전 노드에서 더하기 1을 하여 다음노드를 결정한다. 

    return 0


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    maze=[list(map(int,input())) for _ in range(N)]
    #maze=[list(map(int,input().split())) for _ in range(N)]
    #IndexError: list index out of range
    ca=0
    for i in range(N):
        for j in range(N):
            if maze[i][j]==2:
                r,c=i,j

    result=maze_bfs(r,c)
    print(f"#{tc} {result}")
    






