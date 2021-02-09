#  레벨 1 두 개 뽑아서 더하기
# 정수배열 numbers
# 서로 다른 인덱스에 있는 두 개의 수를 
# 뽑아서 모든 수를 배열에 오름차순으로 return


def solution(numbers):
    answer = []
    
    left = 0
    while left < len(numbers):
        right = left + 1
        while right < len(numbers):
            answer.append(numbers[left] + numbers[right])
            right +=1
        left += 1
    return sorted(set(answer))