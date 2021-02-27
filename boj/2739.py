# 문제 #
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

# 입력 #
# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        N = int(input())
        # [print(f'{N} * {i} = {N*i}') for i in range(1,10)]
        for i in range(1, 10):
            print(f'{N} * {i} = {N*i}')
            

Solution().solution()