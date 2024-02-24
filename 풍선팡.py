# import sys
# sys.stdin = open("input1.txt", "r")
# T = int(input())
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]

#     max_v = 0
#     # cnt=0 #여러개의 값을 뽑아 비교해야 하는데 이러면 모두 다 하나로 합쳐짐
#     for i in range(N):

#         for j in range(M):
#             cnt = arr[i][j]  # cnt+=arr[i][j]: 처음부터 =으로 대입하면 더해주는 효과
#             # 종이 꽃가루 개수만큼 추가로 터짐 즉 첫 풍선에 2개 꽃가루 있었으면 상하좌우 2개씩 다 터짐
#             for d in range(4):

#                 for l in range(arr[i][j]+1):

#                     nr = i+dr[d]*l

#                     nc = j+dc[d]*l

#                 if 0 <= nr < N and 0 <= nc < M:
#                     cnt += arr[nr][nc]
#             if max_v < cnt:

#                 max_v = cnt

#     print(f"#{tc} {max_v}")


arr=[1,2,3,4]
print([0]*len(arr))