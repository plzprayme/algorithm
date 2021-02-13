# 8 x 8
# L자 형태
converter = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8
}

position = input()
col = converter[position[0]]
row = int(position[1])

def move(col, row):
    answer = 0
    # 오른쪽
    if col + 2 < 9:
        # 위
        if row - 1 > 0:
            answer += 1

        # 아래
        if row + 1 < 9:
            answer += 1

    # 왼쪽
    if col - 2 > 0:
        # 위
        if row - 1 > 0:
            answer += 1
        
        # 아래
        if row + 1 < 9:
            answer += 1

    return answer 

answer = move(col, row)
answer += move(row, col)

print(answer)



row = int(position[1])
column = int(ord(position[0])) - int(ord('a')) + 1

# 움직일 수 있는 8가지 방향을 정의한다
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
def solution(steps, row, column):
    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]

        if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
            result += 1


print(solution(steps,row, column))