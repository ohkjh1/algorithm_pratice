import sys
sys.stdin =open('GNS_test_input.txt')
T=int(input())
for tc in range(1,T+1):
    arr=list(map(str,input().split()))
    counts=(9+1)*[0]
   
    solved_arr=len(arr)*[0]#solved_arr=len(arr)*[]
    for i in range(10):#for i in range(10):
        
        counts[arr[i]]+=1

            
    for i in range(1,10):
        counts[i]+=counts[i-1]
    for i in range(len(solved_arr)):
        solved_arr[counts[i]-1]=arr[i]
        counts[i]-=1




    print(tc )
    print(solved_arr)




