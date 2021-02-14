# 맵 N x M 
# 각 칸은 육지 or 바다
# 캐릭터는 동서남북 중 한 곳 바라봄
# (A, B) A는 북쪽으로부터 떨어진 칸의 개수 / B는 서쪽으로 떨어진 칸의 개수
# 바다로는 이동할 수 없다.

# 현자 방향을 기준으로 왼쪽을 항상 먼저 탐색한다.
# 왼쪽에 가보지 않은 칸이 존재한다면 왼쪽 방향으로 회전한 후 한칸 전진
# 왼쪽에 가보지 않은 칸이 없다면 회전만한다.
# 네 반향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우 바라보는 방향을 유지한 채 한칸 뒤로 간 후 1단계로 돌아간다.
# 뒤쪽이 바다라면 움직임을 멈춘다.

# 북 동 남 서
# 0 1 2 3


class Solution():
    direction = 0
    def solution(self):
        def turn_left(d):
            print('TURN LEFT')
            self.direction = self.direction + 1 % 4

        def set_map(row):
            MAP = []
            for row in range(row):
                MAP.append(input().split())
            return MAP

        next_step = {
            0: (1, 0),    # 북
            3: (0, -1),   # 서
            2: (-1, 0),   # 남
            1: (0, 1)     # 동
        }

        row, col  = map(int, input().split())
        y, x, self.direction = map(int, input().split())

        MAP = set_map(row)
        MAP[y][x] = -1

        answer = 0
        while True:
            turn_left(self.direction + 1 % 4)
            position = next_step[self.direction]
            next_y, next_x = y + position[0], x + position[1]

            if MAP[next_y][next_x] == 0: # 육지라면
                print("NEXT_STEP")
                y, x = next_y, next_x    # 다음으로 이동 확정
                MAP[y][x] = -1           # 다음 칸 방문한 곳이라고 체크
                answer += 1              # answer 에 1 증가
                continue

            if MAP[col][row] == 1: # 바다라면
                turn = 0
                for i in range(4):
                    turn += 1
                    turn_left(self.direction + 1 % 4)
                    position = next_step[self.direction]
                    next_y, next_x = y + position[0], x + position[1]
            
                    if MAP[next_y][next_x] == 0: # 육지라면
                        print("NEXT_STEP")
                        y, x = next_y, next_x    # 다음으로 이동 확정
                        MAP[y][x] = -1           # 다음 칸 방문한 곳이라고 체크
                        answer += 1              # answer 에 1 증가
                        break
                
                if turn == 4:
                    position = next_step[self.direction]
                    back_y, back_x = y - position[0], x - position[1]
                    if MAP[back_y][back_x] == 1:
                        return answer
                    
                    turn = 0
                    y, x = back_y, back_x



                continue

        return answer


print(Solution().solution())