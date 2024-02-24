t=int(input())
for tc in range(1,t+1):
    arr=list(map(int,input().split()))
    total=0
    needed=0
    for i in range(1,len(arr)):
        total+=int(arr[i-1]) 
        if i <= total+1:
            needed=i-total

        else:
            continue

    print(f"#{tc} {needed}")