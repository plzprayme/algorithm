# 왼손 엄지는 *  오른손 엄지는 #
# 왼쪽의 1, 4, 7은 무조건 왼손
# 오른쪽의 3,6,9는 무조건 오른손
# 가운데는 가까운 엄지
# 만약 거리가 같다면 오른손 잡이는 오른손/왼손잡이는 왼손


def solution(numbers, hand):
    answer = ''
    left, right = 10, 12

    for num in numbers:
        print(f'left: {left}, right: {right} num: {num} answer: {answer}')
        if num in [1,4,7]:
            answer += 'L'
            left = num
            continue
        
        if num in [3,6,9]:
            answer += 'R'
            right = num
            continue
        
        if num == 0:
            num = 11

        l = abs(left + 2 - num)
        r = abs(right - num)

        if l > r:
            right = num
            answer += 'R'
            continue

        if r > l:
            left = num
            answer += 'L'
            continue

        if hand == 'right':
            right = num
            answer += 'R'
            continue
        else:
            left = num
            answer += 'L'
            continue
        
    return answer

print(solution([1,3,4,5,8,2,1,4,5,9,5], "right")) # "LRLLLRLLRRL"