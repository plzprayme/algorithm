import collections 

def solution(prices):
    prices = collections.deque()

    while prices:
        prices.popleft()
