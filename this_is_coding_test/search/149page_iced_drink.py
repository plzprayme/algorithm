row, col = input().split()
ice = []
for i in range(row):
    ice.append(input().split())

# 상하좌우
direction = [(-1,0), (1,0), (0,-1), (0,1)]

x, y = 0, 0
while True:
    for d in direction: # search()
        next_x, next_y = x + d[1], y + d[0]
        if next_y >= 0 and next_y < row and next_x >= 0 and next_x < row:
            if ice[next_y][next_x] == 0: # search()


    


