import sys
sys.stdin = open("input (9).txt", "r")

dct={
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9

}

# def final_idx_1(word):
#     for i in range(N):
#         for j in range(M-1,0,-1):
#             if info[i][j]==1:
#                 row=i
#                 col=j
#                 return row, col 

def ans():
    for arr in info:
        if '1' in arr:
            after_before=len(arr)-1
            while arr[after_before]=="0":
                after_before-=1


            ca=[]
            for i in range(after_before-55,after_before+1,7):
                ca.append(dct[arr[i:i+7]])


            
            if (sum(ca[0:8:2])*3 +sum(ca[1:8:2]))%10==0:
                return sum(ca[0:8:2]) +sum(ca[1:8:2])
            else:
                return  0
T=int(input())
for tc in range(1,T+1):
    N,M=map(int, input().split())
    info=[input()  for _ in range(N)]

    # print(final_idx_1(info))
    # final_1=final_idx_1(info)[1]
    # final_row=final_idx_1(info)[0]

    a=ans()



    print(f"#{tc} {a}")