import sys
sys.stdin = open("s_input.txt", "r")

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    A,B=map(int,input().split())
    P=int(input())
    #C=int(input())
    
    arr=[0]*5001
    for i in range(N):#for i in range(arr):
        for j in range(A,B+1):
            arr[j]+=1 #arr[i]+=1 위 for를 if로 착각해 이렇게 썼다.
    cnt=0        
    for i in range(P):
        C=int(input())
        if arr[C]>=1:
            cnt=arr[C]
    
    print(f"#{tc} {cnt}")
    
    