# 문제 #
# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

# 입력 #
# 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        N = int(input())
        [print(i+1) for i in range(N)]

Solution().solution()