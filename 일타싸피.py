import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'SEOUL05_KIMCHANBIN'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')


while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.


    #1. white를 구한다. 
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    #2.order==1일 때 내가 맞힐 공의 목록을 구한다. 
    if order == 1:
        for i in [1,3,5]:
            if balls[i][0] == -1:# 해당 공이 없으면 
                continue
            machil_x = balls[i][0]
            machil_y = balls[i][1]
            break
    else:
        for i in [2,4,5]:
            if balls[i][0] == -1:
                continue
            machil_x = balls[i][0]#machil_x좌표
            machil_y = balls[i][1]
            break
          
    # 3.machil공과 가까운 hole을 구한다. 총 홀의 개수는 6개 
         #HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]  
    close_hole = []
    for hole in HOLES:
        d = math.sqrt(abs(hole[0]-machil_x)**2 + abs(hole[1]-machil_y)**2)
     
        close_hole.append(d)

    real_hole = HOLES[close_hole.index(min(close_hole))]
   

    # 4. hole이 machil의 왼쪽 +2*r*탄젠역수 ,위쪽 +2*r*사인의역수를 더하여  화이트볼이 충돌해야 하는 충돌점의 좌표를 구한다.  
    #machil과 hole로 충돌점 구하기 사인의 역수 조심하기 
    r = 2.865
    hole_x = hole[0]
    hole_y = hole[1]

    w = abs(machil_x-hole_x)
    h = abs(machil_y-hole_y)
    pita = math.sqrt(w**2+h**2)

    
    if hole_x <= machil_x: 
        crashx = machil_x+2*r*w/h 
    else: 
        crashx = machil_x-2*r*w/h

    if hole_y <= machil_y:
        crashy = machil_y+2*r*h/pita 
    else:
        crashy = machil_y-2*r*h/pita 

   #5. atan으로 1사분면,2,3,4 화이트가 충돌점의 왼쪽 위쪽에 있을 때 화이트볼과 충돌점의 각도 구하기 
        #화이트볼 충돌점 
        
            #1사  0  2사    
            #90      270  
            #4사 180 3사   
        
    real_w = abs(crashx - whiteBall_x)
    real_h = abs(crashy - whiteBall_y)
    radian = math.atan(real_w / real_h) if real_h > 0 else 0 
    angle = math.degrees(radian)
    #= 180 / math.pi * radian 
    
    #[127, 0]  [127, 127]
    if whiteBall_x == crashx:
        if whiteBall_y < crashy:
            angle = 0
        else:
            angle = 180 
    elif whiteBall_y == crashy:
        if whiteBall_x < crashx: 
            angle = 90 
        else:
            angle = 270
            
            #시계반대방향
            #1사  0  2사    
            #90      270  
            #4사 180 3사
            
    #  2사분면
    if whiteBall_x > crashx and whiteBall_y < crashy:
        radian = math.atan(real_h / real_w)
        angle = 270+(math.degrees(radian))
        #180 / math.pi * radian

    #  3사분면
    if whiteBall_x > crashx and whiteBall_y > crashy: 
        radian = math.atan(real_w / real_h)# 왜 여기만 이렇게 바뀌는질 모르겠음 
        angle = (math.degrees(radian)) + 180
    
    # 4사분면
    elif whiteBall_x < crashx and whiteBall_y > crashy:  
        radian = math.atan(real_h / real_w)
        angle = (math.degrees(radian)) + 90 


    #6. 공격시작 화이트볼과 ex ey
    if order == 1: # 1 , 3 으로 선공 
        if whiteBall_x <= machil_x and whiteBall_y <= machil_y: #이땐 맞힐공으로 조건 주기 / 충돌점의 왼쪽과 위쪽에 있을 때, 화이트볼 1사분면,  
            # 1사분면
            for i in [2,4]:
                flag = 0
                ex, ey = balls[i][0],balls[i][1]
                if whiteBall_x <= ex and whiteBall_y <= ey: # 2, 4가 적인데 이것보다 화이트볼이 좌상에 있을 때 
                    E_width = abs(ex - whiteBall_x)
                    E_height = abs(ey - whiteBall_y) #그 때의 각도와 거리 구하기 
                    E_radian = math.atan(E_width / E_height) if E_height > 0 else 0
                    E_angle = (math.degrees(radian)) - (math.degrees( E_radian))# 이 앵글은 찐 앵글(맞힐공의충돌점과 화이트볼)에서 적과 맞힐공의 앵글을 뺀다. 
                    # distance: 두 점(좌표) 사이의 거리를 계산
                    E_distance = math.sqrt(E_width**2 + E_height**2)

                    if E_distance * math.sin(E_angle) < 2*r: #아무튼 적과 화이트볼이 닿는다면
                        flag = 1
                        break
            if flag == 1:
                continue
                

        elif whiteBall_x >= machil_x and whiteBall_y <= machil_y:
                # 2사분면
            for i in [2,4]:
                flag = 0
                ex, ey = balls[i][0], balls[i][1]
                if whiteBall_x >= ex and whiteBall_y <= ey:
                    E_width = abs(ex - whiteBall_x)
                    E_height = abs(ey - whiteBall_y)
                    E_radian = math.atan(E_width / E_height) if E_height > 0 else 0
                    E_angle = (180 / math.pi * radian) - (180 / math.pi * E_radian)
                    # distance: 두 점(좌표) 사이의 거리를 계산
                    E_distance = math.sqrt(E_width**2 + E_height**2)

                    if E_distance * math.sin(E_angle) < 2*r:
                        flag = 1
                        break
            if flag == 1:
                continue

        elif whiteBall_x >=machil_x and whiteBall_y >= machil_y:
                # 3사분면
            for i in [2,4]:
                flag = 0
                ex, ey = balls[i][0],balls[i][1]
                if whiteBall_x >= ex and whiteBall_y >= ey:
                    E_width = abs(ex - whiteBall_x)
                    E_height = abs(ey - whiteBall_y)
                    E_radian = math.atan(E_width / E_height) if E_height > 0 else 0
                    E_angle = (180 / math.pi * radian) - (180 / math.pi * E_radian)
                    E_distance = math.sqrt(E_width**2 + E_height**2)

                    if E_distance * math.sin(E_angle) < 2*r:
                        flag = 1
                        break
            
            if flag == 1:
                continue

        elif whiteBall_x <= targetBall_x and whiteBall_y >= targetBall_y:
                # 4사분면
            for i in [2,4]:
                flag = 0
                ex, ey = balls[i][0],balls[i][1]
                if whiteBall_x <= ex and whiteBall_y >= ey:
                    E_width = abs(ex - whiteBall_x)
                    E_height = abs(ey - whiteBall_y)

                    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
                    #   - 1radian = 180 / PI (도)
                    #   - 1도 = PI / 180 (radian)
                    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
                    E_radian = math.atan(E_width / E_height) if E_height > 0 else 0
                    E_angle = (180 / math.pi * radian) - (180 / math.pi * E_radian)
                    # distance: 두 점(좌표) 사이의 거리를 계산
                    E_distance = math.sqrt(E_width**2 + E_height**2)

                    if E_distance * math.sin(E_angle) < 2*r:
                        flag = 1
                        break
            if flag == 1:
                continue        

    else:
        if whiteBall_x <= targetBall_x and whiteBall_y <= targetBall_y:
            # 1사분면
            for i in [1,3]:
                flag = 0
                ex, ey = balls[i][0],balls[i][1]
                if whiteBall_x <= ex and whiteBall_y <= ey:
                    E_width = abs(ex - whiteBall_x)
                    E_height = abs(ey - whiteBall_y)

                    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
                    #   - 1radian = 180 / PI (도)
                    #   - 1도 = PI / 180 (radian)
                    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
                    E_radian = math.atan(E_width / E_height) if E_height > 0 else 0
                    E_angle = (180 / math.pi * radian) - (180 / math.pi * E_radian)
                    # distance: 두 점(좌표) 사이의 거리를 계산
                    E_distance = math.sqrt(E_width**2 + E_height**2)

                    if E_distance * math.sin(E_angle) < 2*r:
                        flag = 1
                        break
            if flag == 1:
                continue
                

        elif whiteBall_x >= targetBall_x and whiteBall_y <= targetBall_y:
                # 2사분면
            for i in [1,3]:
                flag = 0
                ex, ey = balls[i][0], balls[i][1]
                if whiteBall_x >= ex and whiteBall_y <= ey:
                    E_width = abs(ex - whiteBall_x)
                    E_height = abs(ey - whiteBall_y)

                    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
                    #   - 1radian = 180 / PI (도)
                    #   - 1도 = PI / 180 (radian)
                    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
                    E_radian = math.atan(E_width / E_height) if E_height > 0 else 0
                    E_angle = (180 / math.pi * radian) - (180 / math.pi * E_radian)
                    # distance: 두 점(좌표) 사이의 거리를 계산
                    E_distance = math.sqrt(E_width**2 + E_height**2)

                    if E_distance * math.sin(E_angle) < 2*r:
                        flag = 1
                        break
            if flag == 1:
                continue

        elif whiteBall_x >= targetBall_x and whiteBall_y >= targetBall_y:
                # 3사분면
            for i in [1,3]:
                flag = 0
                ex, ey = balls[i][0],balls[i][1]
                if whiteBall_x >= ex and whiteBall_y >= ey:
                    E_width = abs(ex - whiteBall_x)
                    E_height = abs(ey - whiteBall_y)

                    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
                    #   - 1radian = 180 / PI (도)
                    #   - 1도 = PI / 180 (radian)
                    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
                    E_radian = math.atan(E_width / E_height) if E_height > 0 else 0
                    E_angle = (180 / math.pi * radian) - (180 / math.pi * E_radian)
                    # distance: 두 점(좌표) 사이의 거리를 계산
                    E_distance = math.sqrt(E_width**2 + E_height**2)

                    if E_distance * math.sin(E_angle) < 2*r:
                        flag = 1
                        break
            
            if flag == 1:
                continue

        elif whiteBall_x <= targetBall_x and whiteBall_y >= targetBall_y:
                # 4사분면
            for i in [1,3]:
                flag = 0
                ex, ey = balls[i][0],balls[i][1]
                if whiteBall_x <= ex and whiteBall_y >= ey:
                    E_width = abs(ex - whiteBall_x)
                    E_height = abs(ey - whiteBall_y)

                    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
                    #   - 1radian = 180 / PI (도)
                    #   - 1도 = PI / 180 (radian)
                    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
                    E_radian = math.atan(E_width / E_height) if E_height > 0 else 0
                    E_angle = (180 / math.pi * radian) - (180 / math.pi * E_radian)
                    # distance: 두 점(좌표) 사이의 거리를 계산
                    E_distance = math.sqrt(E_width**2 + E_height**2)

                    if E_distance * math.sin(E_angle) < 2*r:
                        flag = 1
                        break
            if flag == 1:
                continue     
            
    # distance: 두 점(좌표) 사이의 거리를 계산
    distance = math.sqrt(real_w**2 + real_h**2)

    # power: 거리 distance에 따른 힘의 세기를 계산
    power = distance *0.8


    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    # 
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')