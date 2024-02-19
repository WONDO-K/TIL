import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'E0002_1151174'

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

    # 전략 설명
    # 쿠션을 고려하지 않고 무조건 직선으로 칩니다.
    # 홀을 순회하여 목적구를 중심으로 4분면을 나눠 흰공의 반대방향의 홀을 목표로 하고
    # 목적구에서 홀까지의 거리와 각도를 계산해서 그 거리에서 지름(아마 5.73)만큼 더 나아간 위치를
    # sin과 cos를 사용하여 좌표를 구해서 그 곳을 흰공의 목표로 잡고
    # 흰공과 그곳의 거리와 각도를 구합니다.
    # 목표로 한 공 외에 다른 공은 고려하지 않아 파울은 발생하나 파울로 인해 발생하는 패널티는
    # 일정횟수 이상시에만 발생하고 실제 코드 작동 시 파울을 한 후에 각이 더 좋아지는 경우도 있었기에
    # 그냥 뒀습니다.
    # 거리가 너무 가까울 경우 힘이 거리에 비례해서 치기 때문에 최소값을 50으로 설정했습니다.

    # 두 지점의 각도와 거리 계산
    def get_dis_ang(a, b):
        a_x = a[0]
        a_y = a[1]
        b_x = b[0]
        b_y = b[1]
        width = abs(b_x - a_x)
        height = abs(b_y - a_y)
        # atan2를 이용한 각도 계산
        angle = math.degrees(math.atan2(height,width))
        if angle < 0:
            angle += 360
        # distance: 두 점(좌표) 사이의 거리를 계산
        distance = math.sqrt(width ** 2 + height ** 2)

        return distance, angle


    # 목적지 좌표 계산
    def get_xy(point, distance, angle):
        dis_x = distance * math.cos(math.radians(angle))
        dis_y = distance * math.sin(math.radians(angle))
        x = abs(point[0] - dis_x)
        y = abs(point[1] - dis_y)
        return [x, y]

    # 선공, 후공일 때 목적구 번호
    if order == 1:
        my_balls = [1,3,5]
    else:
        my_balls = [2,4,5]

    # 넣은 공이면 다음 공으로 안 넣은 공이면 멈춤
    for idx in my_balls:
        if balls[idx] == [-1.0,-1.0]:
            continue
        else:
            break
    # 흰공과 x,y 좌표
    whiteBall = balls[0]
    whiteBall_x = whiteBall[0]
    whiteBall_y = whiteBall[1]

    # 목적구와 x,y 좌표
    targetBall = balls[idx]
    targetBall_x = targetBall[0]
    targetBall_y = targetBall[1]

    # 홀을 순회, 목적구를 중심으로 필드를 4등분, 흰공의 반대편 홀을 목표로 함
    for hole in HOLES:
        if targetBall_x >= whiteBall_x and targetBall_y >= whiteBall_y:
            if targetBall_x <= hole[0] and targetBall_y <= hole[1]:
                break
        elif targetBall_x >= whiteBall_x and targetBall_y < whiteBall_y:
            if targetBall_x <= hole[0] and targetBall_y > hole[1]:
                break
        elif targetBall_x < whiteBall_x and targetBall_y >= whiteBall_y:
            if targetBall_x > hole[0] and targetBall_y <= hole[1]:
                break
        elif targetBall_x < whiteBall_x and targetBall_y < whiteBall_y:
            if targetBall_x > hole[0] and targetBall_y > hole[1]:
                break

    # 홀과 목적구의 거리와 길이
    t_h_d, t_h_a = get_dis_ang(targetBall, hole)
    # 흰공의 목적지
    w_target = get_xy(hole,t_h_d+5.73,t_h_a)

    # 목적지와 흰공의 각도와 거리 계산
    w_target_x = w_target[0]
    w_target_y = w_target[1]

    # width, height: 목적지와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width = abs(w_target_x - whiteBall_x)
    height = abs(w_target_y - whiteBall_y)

    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
    #   - 1radian = 180 / PI (도)
    #   - 1도 = PI / 180 (radian)
    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
    radian = math.atan(width / height) if height > 0 else 0
    angle = 180 / math.pi * radian

    # 목적지가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력
    if whiteBall_x == w_target_x:
        if whiteBall_y < w_target_y:
            angle = 0
        else:
            angle = 180
    elif whiteBall_y == w_target_y:
        if whiteBall_x < w_target_x:
            angle = 90
        else:
            angle = 270

    # 목적지가 흰 공을 중심으로 1사분면에 위치했을 때 각도를 계산
    if whiteBall_x < w_target_x and whiteBall_y < w_target_y:
        radian = math.atan(width / height)
        angle = (180 / math.pi * radian)

    # 목적지가 흰 공을 중심으로 2사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x > w_target_x and whiteBall_y < w_target_y:
        radian = math.atan(height / width)
        angle = (180 / math.pi * radian) + 270

    # 목적지가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x > w_target_x and whiteBall_y > w_target_y:
        radian = math.atan(width / height)
        angle = (180 / math.pi * radian) + 180

    # 목적지가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x < w_target_x and whiteBall_y > w_target_y:
        radian = math.atan(height / width)
        angle = (180 / math.pi * radian) + 90

    # distance: 두 점(좌표) 사이의 거리를 계산
    distance = math.sqrt(width**2 + height**2)

    # power: 거리 distance에 따른 힘의 세기를 계산
    power = distance * 0.5
    power = max(power,50)
    
        

    # # 70점 확보 코드
    # # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    # whiteBall_x = balls[0][0]
    # whiteBall_y = balls[0][1]
    #
    # # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    # # 1번 공을 넣으면 1번을 3번으로 변경
    # if balls[1] == [-1.0,-1.0]:
    #     balls[1] = balls[3]
    #
    # targetBall_x = balls[1][0]
    # targetBall_y = balls[1][1]
    #
    # # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    # width = abs(targetBall_x - whiteBall_x)
    # height = abs(targetBall_y - whiteBall_y)
    #
    # # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
    # #   - 1radian = 180 / PI (도)
    # #   - 1도 = PI / 180 (radian)
    # # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
    # radian = math.atan(width / height) if height > 0 else 0
    # angle = 180 / math.pi * radian
    #
    # # 목적구가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력
    # if whiteBall_x == targetBall_x:
    #     if whiteBall_y < targetBall_y:
    #         angle = 0
    #     else:
    #         angle = 180
    # elif whiteBall_y == targetBall_y:
    #     if whiteBall_x < targetBall_x:
    #         angle = 90
    #     else:
    #         angle = 270
    #
    # # 목적구가 흰 공을 중심으로 1사분면에 위치했을 때 각도를 계산
    # if whiteBall_x < targetBall_x and whiteBall_y < targetBall_y:
    #     radian = math.atan(width / height)
    #     angle = (180 / math.pi * radian)
    #
    # # 목적구가 흰 공을 중심으로 2사분면에 위치했을 때 각도를 재계산
    # elif whiteBall_x > targetBall_x and whiteBall_y < targetBall_y:
    #     radian = math.atan(height / width)
    #     angle = (180 / math.pi * radian) + 270
    #
    # # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
    # elif whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
    #     radian = math.atan(width / height)
    #     angle = (180 / math.pi * radian) + 180
    #
    # # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
    # elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
    #     radian = math.atan(height / width)
    #     angle = (180 / math.pi * radian) + 90
    #
    # # distance: 두 점(좌표) 사이의 거리를 계산
    # distance = math.sqrt(width**2 + height**2)
    #
    # # power: 거리 distance에 따른 힘의 세기를 계산
    # power = distance * 0.5






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