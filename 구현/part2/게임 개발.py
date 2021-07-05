n, m = map(int, input().split())

# 방문했던 위치를 넣을 d 생성, 0으로 초기화
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 현재 맵을 넣:을 array 생성
array = []
for i in range(n)
    array.append(list(map(int,input().split())))


# 북, 동, 남, 서 방향 정의 
# 0, 1, 2, 3
dx = [-1, 0, 1, 0] # 세로
dy = [0, 1, 0, -1] # 가로

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    # 0이 끝이므로 -1이 되면 한 바퀴 돌리기
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 기존과 정면 모두 0일 때 count를 늘린다.
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전 후 정면이 1일 때
    else:
        # 한 번 더 돌린다
        turn_time += 1
    # 4번 돌려본 결과 상하좌우 모두 갈 수 없을 때 
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있으면 이동해서 다시 시작
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다면 끝내기
        else:
            break
        turn_time = 0

print(count)
