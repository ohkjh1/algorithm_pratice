from collections import deque
T=1
for _ in range(1,T+1):
    tc=int(input())
    q=deque(map(int,input().split()))
    
    cnt=0
    while True:
        cnt+=1
        selected=q.popleft()-cnt
        if cnt==5:
            cnt=0
        #print(selected)
        if selected<=0:
            q.append(0)
            break
        else:
            q.append(selected)
    print(f"#{tc} ", end=" ")
    for i in range(8):
        print(f"{q[i]} ", end=" ")
    print()



