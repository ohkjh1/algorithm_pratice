dc=[1,0,-1,0]
dr=[0,1,0,-1]

def dfs(r,c):
    global possible
    if mazeArray[r][c]==3:
        possible=1
    mazeArray[r][c]=1
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and mazeArray[nr][nc] != 1:
            dfs(nr,nc)

T=int(input())
for tc in range(1, T + 1):
    N = int(input())

    mazeArray = [list(map(int, input())) for _ in range(N)]
    possible = 0

    for i in range(N):
        for j in range(N):
            if mazeArray[i][j] == 2:
                r = i
                c = j

    dfs(r, c)
    print(f"#{tc} {possible}")