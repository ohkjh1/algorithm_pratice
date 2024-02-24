

def fibo(n):
    lst=[0]*(n+1)
    lst[1]=1
    lst[2]=3
    for i in range(3, n+1):
        lst[i]=lst[i-1]+2*lst[i-2]
    return lst[n]
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    n=N//10
    
    
    
    print(f"#{tc} {fibo(n)}")
