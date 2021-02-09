def solution(board, moves):
    def get_doll(col):
        for j in range(N):
            if 0 != board[j][col]:
                doll = board[j][col]
                board[j][col] = 0
                return doll
        return -1
    
    def put_doll(doll):
        try:
            if moved[len(moved)-1] == doll:
                moved.pop()
                return 2
        except IndexError:
            pass
        
        moved.append(doll)
        return 0


    answer = 0
    N = len(board)
    moved = []

    for i in moves:
        doll = get_doll(i-1)
        if doll == -1:
            continue
        answer += put_doll(doll)
    return answer

print(solution([[0,0,0,0,0], 
                [0,0,1,0,3],
                [0,2,5,0,1],
                [4,2,4,4,2],
                [3,5,1,3,1]], [1,5,3,5,1,2,1,4]))