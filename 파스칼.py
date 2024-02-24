# arr=[1,1]
# for i in range(1,4):
#     for j in range(i):
#         arr=[1]+[arr[i-1][j]+arr[i-1][j+1]]+[1]

# 조합을 DP로 구함
SIZE = 100
memo = [[0] * SIZE for _ in range(SIZE)]
for i in range(SIZE):


    for j in range(i+1):
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i-1][j-1] + memo[i-1][j]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(memo[i][j], end=' ')
        print()
    # print(memo[50][25])