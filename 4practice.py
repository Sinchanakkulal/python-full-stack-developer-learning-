items=[1,2,3,"hello",6,5]

#Add a new item to the end of the list and another at the second position.
items.append("world")
print(items)
items.insert(1,1)
print(items)

#Remove the third item from the list.
items.pop(2)
print(items)

num=[5,2,8,3,4]
#Sort it in descending order.
# num.sort(reverse=True)
# print(num)
sorted_num=sorted(num)
reversed_sorted_num=sorted_num[::-1]
print(reversed_sorted_num)

tup=tuple("geeks")
print(tup[0])
print(tup[0:4])

# Tuple unpacking
tup=("geeks","world","python")

# This line unpack values of Tuple1
a,b,c=tup
print(a)
print(b)
print(c)

#concatenation of tuples
tup1=(0,1,2)
tup2=(3,4,5)
print(tup1+tup2)

# del tup
# print(tup) #this will give error as tup1 is deleted

print((1, 2, 3) + (4, 5, 6))