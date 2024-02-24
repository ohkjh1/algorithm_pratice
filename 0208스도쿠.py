T=int(input())
for tc in range(1,T+1):
    check_subject=[list(map(int,input().split())) for _ in range(9)]#리스트 하나씩 만들어서 새로운 큰 리스트 안으로 
    check=[1,2,3,4,5,6,7,8,9]
    judge=1
    for i in range(9):
        sep_row=[]
        for j in range(9):
            sep_row.append(check_subject[i][j])
        sep_row.sort()
        if sep_row!=check:
            judge=0
    for i in range(9):
        sep_col=[]
        for j in range(9):
            sep_col.append(check_subject[j][i])
        sep_col.sort()
        if sep_col!=check:
            judge=0
    for i in range(9):
        sep_3_3=[]
        for j in range(3):
            for k in range(3):
                sep_3_3.append(check_subject[(i//3)*3+j][(i%3)*3+k]) # 각 i에 대해 j이고 각 j에 대해 k이다
                #i==0 j==0,1,2 j==0 k=0,1,2((012)) i==1(실제0) j=0,1,2 k=0,1,2((345))0행의 345 열 1행의 345열 2행의 345열 
        sep_3_3.sort()
        if sep_3_3 != check:
            judge=0
    print(f"#{tc} {judge}")    




