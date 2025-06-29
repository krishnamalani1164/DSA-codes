from collections import deque

def interleave_queues(q1, q2):
    result = deque()
    
    while q1 or q2:
        if q1:
            result.append(q1.popleft())
        if q2:
            result.append(q2.popleft())
    
    return result

q1 = deque([1, 3, 5])
q2 = deque([2, 4, 6, 8])

interleaved = interleave_queues(q1, q2)
print("Interleaved Queue:", list(interleaved))