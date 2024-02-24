T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    #M번 이동,N개의 자연수 
    arr=list(map(int,input().split()))+[0]*1000
    #M<=1000 최대 1000번 이하 돌릴 것임
    front=-1
    rear=N-1
    for i in range(M):
        front+=1
        rear+=1
        arr[rear]=arr[front]
        # arr[front]=0
        # print(arr)

        

    print(f"#{tc} {arr[front+1]} ")
    #처음 rear 현재의 마지막 항이 나오겠지
    #front만 썼더니 새로운 정렬의 첫항이 나오지 않고 이전의 첫항이 나옴 
    #arr[front]=0으로 초기화해주면 확인이 쉬움, 0이 되어있음 ,  왜냐면 그 부분을 1증가시켜 뒤로 보냈으니깐 
    #front+=1했더니 비로소 첫 항이 나옴 