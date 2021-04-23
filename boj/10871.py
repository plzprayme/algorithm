# 문제 #
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다
# A에서 X보다 작은 수를 모두 출력하는 프로그램 작성

# 입력 #
# 첫째 줄에 N과 X
# 둘때 줄에 A를 이루는 정수 N개

import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        # N, X = map(int, input().split())
        # result = [i for i in map(int, input().split()) if i < X]
        # [print(i, end=' ') for i in result]
        # print(result[-1], end=' ')

        N, X = map(int, input().split())
        A = map(int, input().split())
        A = [print(i, end=' ') for i in filter(lambda i: i < X, A)]

Solution().solution()
    
