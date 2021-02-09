# 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램
# 아이디 길이 3 ~ 15
# 알파벳 소문자, 숫자, -, _, . 만 사용 가능
# .는 처음과 끝에서 사용 불가 / 연속 사용 불가

def solution(new_id):
    answer = ''

    # step_1 ~ 2
    for i in new_id:
        for j in i:
            if j.isupper():
                answer += j.lower()
                continue

            if j.islower():
                answer += j
                continue

            if j.isdigit():
                answer += j
                continue

            if j == '-' or j == '_' or j == '.':
                answer += j
                continue
    
    
    

    cnt = 0
    answer2 = ''
    for i in range(len(answer)):
        val = answer[i]
        if val != '.':
            answer2 += val
            cnt = 0
            continue

        if cnt != 0:
            continue

        cnt += 1
        answer2 += val

    # print(answer2)

    # s4
    if answer2[0] == '.':
        answer2 = answer2[1:]

    if answer[-1] == '.':
        answer2 = answer2[:-1]
        # print(answer2)

    

    # s5
    if len(answer2) == 0:
        return 'aaa'



    # s6
    if len(answer2) > 15:
        answer2 = answer2[:15]


    if answer2[-1] == '.':
        answer2 = answer2[:-1]

    # s7
    # if len(answer2) < 2:
    while len(answer2) < 3:
        answer2 += answer2[-1]

    return answer2


# print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution(	"z-+.^."))
