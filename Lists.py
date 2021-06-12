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

list1 = [1,2,3,4,5]
list2 = [4,5,6,7]
templist = list1
print(id(list1))
list1 += list2
print(id(list1))
list1 += [8]
list1.append(9)
list1.insert(12,10)
templist.insert(13,11)
print(list1)
print(f"This is temp list {templist}")
print(id(templist))
print(id(list1))



