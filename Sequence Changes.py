list1 = [[]]*5
list3 = [[] for i in range(4)]
list1[0] += [5,6,7,8,9,10]
list1[1] += [500,600,700]
list3[0] += [5,6,7,8,9,10]
list3[1] += [500,600,700]

list2 = [1,2,3,5] and [1,2,3,4]
print(list1)
print(list2)
print(list3)
print(list3[1][0])
list2 = []
print(f"after deleting{list2}")

elec_gadget = ["computer","Music system","video player","Gaming Console"]
for gindex,gitem in enumerate(elec_gadget):
    print(f"The item id is {gindex+1} and item is {gitem}")
