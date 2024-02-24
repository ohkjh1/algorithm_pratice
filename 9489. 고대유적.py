#import sys; sys.stdin=open("input (2).txt","r")
t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split())#n개 줄 m개 열 
    info=[list(map(int,input().split())) for i in range(n)]
    max_val=0
    for r in range(n):#행이 기준이 됨 0 행 - 0열 , 1열,2열
        cnt=0 #cnt 지금 가로 하나씩만 계산할 거임 즉 cnt초기화는 가로 시작할 때마다 초기화 
        # 1이면 끝까지 해서cnt 하나에 다 더할까봐 이렇게 했는데
        #생각해보니 0일 때 cnt=0으로 초기화해주면 
        #이럴 필요가 없다 
        #심지어 인덱스 아웃오브레인지도 발생함 
        # for c in range(1,m+1):
        #     if info[r][c-1]==info[r][c] and info[r][c-1] ==1 :
        #         cnt+=1
        #     elif info[r][c-1]!=info[r][c] and info[r][c-1] ==1:
        #         cnt+=0
        #     else:
        #         cnt=0

        for c in range(m):
            if info[r][c]==1:
                cnt+=1
                if cnt>max_val:
                    max_val=cnt
            else:
                cnt=0#여기서 1이 이어지지 않을 때 한 번 끊어줌 
        # if cnt>max_val:
        #     max_val=cnt
        #     print(max_val)

    for c in range(m): #여기만 이렇게 바꿔주면 열이 기준 0행, 1행, 2행 - 0열
        cnt=0
        
        for r in range(n):
            if info[r][c] ==1:
                cnt+=1
                if cnt > max_val:
                    max_val=cnt

            else:
                cnt=0
        # if cnt > max_val:
        #     max_val=cnt
        #     print("세로", max_val)
    print(f"#{tc} {max_val}")#{cnt} 이렇게 쓰면 안된다 기껏 max_val에 넣어놓고 