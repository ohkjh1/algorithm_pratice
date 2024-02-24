T=10
for tc in range(1,T+1):
    N = int(input())
    finding=input()
    area=input()

    f_idx=0
    a_idx=0
    f_len=len(finding)
    a_len=len(area)

    involved_cnt=0

    while   f_idx<f_len and a_idx<a_len : #인덱스는 0부터 시작 같으면은 안된다
        if  finding[f_idx] != area[a_idx]:
            a_idx = a_idx-f_idx #이제까지 비교한 거 바로 다음으로 가야하니까 
            #f_idx는 같지 않으면 자신의 첫 인덱스로 돌아감 
            #안 돌아가고 있다면 그건 a_idx와 비교한 횟수 
            #전체 idx에서 비교한 횟수 빼서 바로 다음 인덱스로 간다 
            f_idx=-1 # while 구문에서 if 끝나면 1을 더해줄 거라서 0이 되어 처음으로 돌아가는 것이 됨 
        # else라 생각 같으면 그냥 일 더해주기 두 인덱스 모두에 
        a_idx = a_idx+1
        f_idx= f_idx+1

        #이렇게 해서 f_idx 개수가 그 지금 finding 글자수만큼 갔다면 
        #area문자열에서 finding 문자열을 찾았다는 말 
        #여기까지 왔다는 것은 위의 if 문 같지 않음에 해당된 적이 없었다는 말 
        #f_idx 가 0부터 시작했으므로 0 1 2 3 len=3 이렇게 
        if f_idx == f_len:#?
            involved_cnt+=1
            #즉 처음 0으로 시작해서 위의 if 안 거치고 여까지 왔다면 
            #a_idx 에서 f_idx 횟수를 뺀 후 그  다음부터 검색 시작 
            f_idx = 0 
            a_idx -= f_idx#?
            
            
    result=involved_cnt    

    print(f"#{tc} {result}")
            

