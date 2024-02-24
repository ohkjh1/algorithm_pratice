import sys
sys.stdin = open("input (7).txt", "r")

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    
    result=0

    for i in range(len(arr)):
        _sum=sum(arr[i:-1])
        if int(arr[-1]) > _sum:
            result=int(arr[-1])*len(arr[i:-1])-_sum

        else:
            result=0

    print(f"#{tc} {result}")

