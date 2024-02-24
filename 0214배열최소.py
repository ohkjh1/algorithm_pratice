def perm(i,s):
    global min_v
    global N
    #global N
    #global N 왜 안해줘도 N을 함수 내에서 쓸 수 있는가 ? 
    #함수 내에서 변경을 하질 않으니까 결과에 영향이 없다 
    
    #selected=[[0]*N]
    #selected=[0]*N 이게 왜 여기에 있으면 안될까>? 재귀로 호출할 때마다 아예 다 새로워짐 
    #원래는 한 줄하면서 그 전 열 0으로 만들고 또 다음 한 줄 하면서 그 전 열 0으로 만들고 이렇게 해야함  
    #즉 전역변수로 해야할 듯 

    if s>min_v:
        return

    if i == N :
        if s<min_v:
            min_v=s
        else:
            return 



    for j in range(N):
        if not selected[j]:
            selected[j]=1#selected[i][j]=1
            perm(i+1,s+arr[i][j])
            selected[j]=0 #selected[i][j]=0





T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    min_v=100
    selected=[0]*N

    perm(0,0)

    print(f"#{tc} {min_v}")