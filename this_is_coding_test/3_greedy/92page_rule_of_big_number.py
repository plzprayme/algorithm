# 다양한 수로 이루어진 배열이 있을 때
# 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
# 특정 인덱스의 숫자가 연속해서 K번을 더할 수 없다.

# 배열의 크기, 더하는 횟수, 연속할 수 있는 횟 수

# case 1
N, M, K = 5, 8, 3
nums = [2,4,5,4,6]

# case2
# N, M, K = 5, 7, 2
# nums = [3,4,3,4,3]

def my_solution():
    nums.sort(reverse=True)
    bigger = nums[0]
    smaller = nums[1]

    smaller_multiply = M//K
    bigger_multiply = M - smaller_multiply


    answer = 0
    answer += nums[0] * bigger_multiply
    answer += nums[1] * smaller_multiply
    return answer

if __name__ == '__main__':
    print(my_solution())
    