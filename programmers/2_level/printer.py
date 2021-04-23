import collections

def solution(priorities, location):
    q = collections.deque(priorities)

    cnt = 0
    while True:
        if q[0] < max(q):
            if location == 0:
                location += len(q) - 1
            else:
                location -= 1

            q.append(q.popleft())

        else:
            if location == 0:
                return cnt + 1
            q.popleft() 
            cnt += 1
            location -= 1

    

    

print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))