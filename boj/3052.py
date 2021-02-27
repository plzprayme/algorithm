# 문제 #
# 수 10개를 입력받은 후 42로 나눈 나머지를 구한다.
# 서로 다른 값이 몇개 있는지 출력한다.

import sys
import collections
class Solution:
    input = sys.stdin.readline
    def solution(self):
        remain = [int(input()) % 42 for i in range(10)]
        return len(collections.Counter(remain))

print(Solution().solution())
