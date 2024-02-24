import sys
sys.stdin = open("input (3).txt", "r")


T=10
for T in range(1,T+1):
    N,s=map(int,input().split())

    lst=str(s)

    stack=[]


    for data in lst:
        if len(stack)!=0 and data==stack[-1]:
            stack.pop()
        else:
            stack.append(data)
    
            
	
    print(f"#{T} { ''.join(str(s) for s in stack)} ")