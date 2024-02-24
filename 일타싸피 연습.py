import math
while True:
    #1. 화이트볼 좌표 
    white_x=balls[0][0]
    white_y=balls[0][1]
    #2. 맞힐 타겟볼 좌표 
    if order==1:

        for i in [1,3,5]:
            if balls[i][0]==-1:
                continue
            target_x=balls[i][0]
            target_y=balls[i][1]
            break
    else:
        for i in [2,4,5]:
            target_x=balls[i][0]
            target_y=balls[i][1]
            break

    #3. 타켓볼과 가까운 홀 좌표 
    close_hole=[]
    for hole in HOLES:
        d=math.sqrt((hole[0]-target_x)**2+(hole[1]-target_y)**2) 
        close_hole.append(d)
    real_hole=close_hole[close_hole.index(min(close_hole))]

    #4. 홀좌표와 타겟볼좌표를 이용한 충돌점좌표
    w=abs(real_hole[0]-target_x)
    h=abs(real_hole[1]-target_y)
    pita=math.sqrt(w**2+h**2)
    r=2.8
    #cos, sin
    if real_hole[0]<=target_x:
        crash_x=target_x+2*r*w/pita
    else:
        crash_x=target_x-2*r*w/pita

    if real_hole[1]<=target_y:
        crash_y=target_y+2*r*h/pita
    else:
        crash_y=target_y-2*r*h/pita

    #5. 화이트좌표와 충돌점좌표를 이용한 각도 

    real_w=abs(white_x-crash_x)
    real_h=abs(white_y-crash_y)
    radian=math.atan(real_w/real_h) if real_h > 0 else 0 
    angle=math.degrees(radian)

    if white_x == crash_x:
        if white_y<crash_y:
            angle=0
        else:
            angle=180
    if white_y==crash_y:
        if white_x<crash_x:
            angle=90
        else:
            angle=270


    #2사분면 각도 교체  2사분면에 있을 때 2사분면 위치에서 공을 치나보다 
    if white_x > crash_x and white_y < crash_y:
        angle=270+math.degrees(math.atan(real_h/real_w))#1.3.마지막w/h ? 2.4h/w

    #3사분면 각도 교체 
    if white_x > crash_x and white_y > crash_y:
        angle=180+math.degrees(math.atan(real_w/real_h))

    #4사분면 각도 교체 
    if white_x < crash_x and white_y>crash_y:
        angle=90+math.degrees(math.atan(real_h/real_w))



    #6. 공을 칠 때 제한사항  ex와 화이트간의 거리 
    #1사분면 
    if order==1:
        if white_x <= target_x and white_y<=target_y:
            for i in [2,4]:
                flag=0
                ex=balls[i][0]
                ey=balls[i][1]
                if white_x <= ex and white_y <=ey:
                    ew=abs(white_x-ex)
                    eh=abs(white_y-ey)
                    epita=math.sqrt(ew**2+eh**2)
                    eradian=math.atan(ew/eh) if eh > 0 else 0
                    limit_angle=math.degrees(radian)-math.degrees(eradian)
                    if epita*math.sin(limit_angle) < 2*r:
                        flag=1
                        break
            if flag == 1:
                continue

        #2사분면         
        elif white_x >= target_x and white_y<=target_y:
            for i in [2,4]:
                flag=0
                ex=balls[i][0]
                ey=balls[i][1]
                if white_x >= ex and white_y <=ey:
                    ew=abs(white_x-ex)
                    eh=abs(white_y-ey)
                    epita=math.sqrt(ew**2+eh**2)
                    eradian=math.atan(ew/eh) if eh > 0 else 0
                    limit_angle=math.degrees(radian)-math.degrees(eradian)
                    if epita*math.sin(limit_angle) < 2*r:
                        flag=1
                        break
            if flag == 1:
                continue


        #3사분면         
        elif white_x >= target_x and white_y>=target_y:
            for i in [2,4]:
                flag=0
                ex=balls[i][0]
                ey=balls[i][1]
                if white_x >= ex and white_y >=ey:
                    ew=abs(white_x-ex)
                    eh=abs(white_y-ey)
                    epita=math.sqrt(ew**2+eh**2)
                    eradian=math.atan(ew/eh) if eh > 0 else 0
                    limit_angle=math.degrees(radian)-math.degrees(eradian)
                    if epita*math.sin(limit_angle) < 2*r:
                        flag=1
                        break
            if flag == 1:
                continue



        elif white_x <= target_x and white_y>=target_y:
            for i in [2,4]:
                flag=0
                ex=balls[i][0]
                ey=balls[i][1]
                if white_x <= ex and white_y >=ey:
                    ew=abs(white_x-ex)
                    eh=abs(white_y-ey)
                    epita=math.sqrt(ew**2+eh**2)
                    eradian=math.atan(ew/eh) if eh > 0 else 0
                    limit_angle=math.degrees(radian)-math.degrees(eradian)
                    if epita*math.sin(limit_angle) < 2*r:
                        flag=1
                        break
            if flag == 1:
                continue


    else:
        if white_x <= target_x and white_y<=target_y:
            for i in [1,3]:
                flag=0
                ex=balls[i][0]
                ey=balls[i][1]
                if white_x <= ex and white_y <=ey:
                    ew=abs(white_x-ex)
                    eh=abs(white_y-ey)
                    epita=math.sqrt(ew**2+eh**2)
                    eradian=math.atan(ew/eh) if eh > 0 else 0
                    limit_angle=math.degrees(radian)-math.degrees(eradian)
                    if epita*math.sin(limit_angle) < 2*r:
                        flag=1
                        break
            if flag == 1:
                continue

        #2사분면         
        elif white_x >= target_x and white_y<=target_y:
            for i in [1,3]:
                flag=0
                ex=balls[i][0]
                ey=balls[i][1]
                if white_x >= ex and white_y <=ey:
                    ew=abs(white_x-ex)
                    eh=abs(white_y-ey)
                    epita=math.sqrt(ew**2+eh**2)
                    eradian=math.atan(ew/eh) if eh > 0 else 0
                    limit_angle=math.degrees(radian)-math.degrees(eradian)
                    if epita*math.sin(limit_angle) < 2*r:
                        flag=1
                        break
            if flag == 1:
                continue


        #3사분면         
        elif white_x >= target_x and white_y>=target_y:
            for i in [1,3]:
                flag=0
                ex=balls[i][0]
                ey=balls[i][1]
                if white_x >= ex and white_y >=ey:
                    ew=abs(white_x-ex)
                    eh=abs(white_y-ey)
                    epita=math.sqrt(ew**2+eh**2)
                    eradian=math.atan(ew/eh) if eh > 0 else 0
                    limit_angle=math.degrees(radian)-math.degrees(eradian)
                    if epita*math.sin(limit_angle) < 2*r:
                        flag=1
                        break
            if flag == 1:
                continue



        elif white_x <= target_x and white_y>=target_y:
            for i in [1,3]:
                flag=0
                ex=balls[i][0]
                ey=balls[i][1]
                if white_x <= ex and white_y >=ey:
                    ew=abs(white_x-ex)
                    eh=abs(white_y-ey)
                    epita=math.sqrt(ew**2+eh**2)
                    eradian=math.atan(ew/eh) if eh > 0 else 0
                    limit_angle=math.degrees(radian)-math.degrees(eradian)
                    if epita*math.sin(limit_angle) < 2*r:
                        flag=1
                        break
            if flag == 1:
                continue


    distance=math.sqrt(real_w**2+real_h**2)
    power=distance*0.8  
    result=f"{angle} {power}"
    sock.send(result.encode('utf-8'))
    print(f'dataSent : {result}')


        
sock.close()