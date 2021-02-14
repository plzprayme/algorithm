# 비밀지도
# n x n 공백 or #(벽)

# 두장 겹쳐서 모두 공백이면 공백 



def solution(n, arr1, arr2):
    result = []
    for row1, row2 in zip(arr1, arr2):
        answer = ''
        row1 = bin(row1)[2:].zfill(n)
        row2 = bin(row2)[2:].zfill(n)
        
        for _row1, _row2 in zip(row1, row2):
            if _row1 == '0' and _row2 == '0':
                answer += ' '
            else:
                answer += '#'
        result.append(answer)

    return result


# print(solution(5, [9,20,28,18,11], [30,1,21,17,28])) # "#####", "# # #", "# ##", "#####"
print(solution(6, [46,33,33,22,31,50], [27,56,19,14,14,10])) # "######", "### #", "## ##", " #### ", " #####", "### # "