
def postorder(t):
    if 0<t<=N:
        if tree[t]==0:#노드 정점의 값이 없을때, 아직 노드값이 정해지지 않음 
            #int ,nontype error 나와서 int 씌워줌 - X
            # tree[t]=int(postorder(2*t))+int(postorder(2*t+1))
            #밑에 return tree[t] 이게 있어야 한다 노드가 안비어있으면 그 값을 반환 
            tree[t]=postorder(2*t)+postorder(2*t+1)
            #t는 정점 노드 
            #여기서 계속 돌다가 
            #만약 리프노드를 만나면 
            #tree[t]!=0 이라서 tree[t]를 반환하고 그 값(좌우)들을 더하게 됨 
        return tree[t]
    else:
        return 0#총 노드 개수 벗어나면 당연히 0으로 




T=int(input())
for tc in range(1,T+1):
    N,M,L=map(int,input().split())
    #node,val=map(int,input().split()) for _ in range(M)
    tree=[0]*(N+1)
    for _ in range(M):
        node,val=map(int,input().split())
        tree[node]=val
    #tree[node]=val
    #여기에 하면 안되죠tree=[0]*(N+1)



    postorder(1)


    print(f"#{tc} {tree[L]}")

