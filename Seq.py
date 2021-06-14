import timeit

strlist = "feDcbA"
print(sorted(strlist,reverse=True))
print("After sorting the list\n")
newlist = sorted(strlist,key=str.casefold,reverse=True)

print(newlist)

even_list = [2,4,6,8,10]
odd_list = [1,3,5,7,9]

new_list = even_list+odd_list
sorted_list = sorted(new_list)
lst = new_list.copy()
lst2 = [*new_list]
print(id(lst))
print(id(lst2))
print(id(sorted_list))
print(id(new_list))

odd_list[2:4] = [11,13,15]
print(odd_list)




