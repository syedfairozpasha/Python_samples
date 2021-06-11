from collections import deque
listx = [1,2,2,4]
rev =[]
print(f"type is {type(rev)}")
print(listx.reverse())

quex = deque(listx)
quex.append(5)
print(f"After appending {quex}")
quex.popleft()
print(f"after poping left {quex}")
quex.appendleft(10)
print(f"after adding to left {quex}")


