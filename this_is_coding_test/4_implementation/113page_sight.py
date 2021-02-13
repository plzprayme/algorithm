# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지
# 3이 하나라도 포함되는 모든 경우의 수를 구하라

N = int(input())

three = '3'
answer = 0
for n in range(N+1):
    for m in range(60):
        for s in range(60):
            if three in str(n) or three in str(m) or three in str(s):
                answer += 1
                continue

print(answer)
