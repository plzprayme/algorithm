# N X N / 1 X 1
# (1, 1) / (N, N)

# 5
# R R R U D D
direction = []
direction = input().split(" ")

x, y = 0, 0
for d in direction:
    if d == 'R':
        x += 1
    elif d == 'L':
        x -= 1
    elif d == 'U':
        y += 1
    elif d == 'D':
        y -= 1

print(x, y)