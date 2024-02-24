T = int(input())


# i번쨰 행에 대해서 j번째 열을 골라서 합을 만든다.
# 대신 j는 중복해서 고르면 안된다.
def perm(i, now_sum):
    global min_v
    

    # 0. 가지치기(최적화)
    # 현재 내가 i번 행까지 구한 합이 이전에 구한 최소합보다 크면 더 진행할 필요 x
    if now_sum > min_v:
        return
    #그전의 모든 행을 통과한 합이 min_v로 저장되어 있기 때문에 현재 한줄씩 더해가는 과정에서 만약 
    # 그전 모든 행을 통과한 합보다 크게 되면 볼 필요가 없이 
    #왜냐면 지금 1열 2열 3열 다 돌아가면서 처음에 1열을 선태하고 밑으로 내려감 또 2열을 선택하고 밑으로 내려감 

    # 1. 종료 조건
    if i == N:
        # i가 N이되면 다 고른거다.
        if now_sum < min_v:
            min_v = now_sum
        return

    # 2. 재귀 호출
    # 0 ~ N-1 번째 열 중에서 이전에 고른적이 없는 j번 열을 선택하기
    for j in range(N):
        # j번 열을 고른적이 없는지 확인
        if not selected[j]:
            # j 번째 열을 i번째 행에서 골랐다고 표시 하고 i+1번째 행으로 넘어간다.
            selected[j] = 1
            perm(i + 1, now_sum + arr[i][j])
            # j번 골랐던거 다 계산하고 다음을 위해 초기화
            selected[j] = 0


for tc in range(1, T + 1):
    # 배열의 크기, N * N
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 열을 중복해서 선택하면 안되니까 중복 체크 배열
    selected = [0] * N
    min_v = 100
    
    # 0번 행부터 고르기 시작하고, 합도 0에서 시작
    perm(0, 0)

    print(f"#{tc} {min_v}")
