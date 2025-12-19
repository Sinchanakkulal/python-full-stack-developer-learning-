# num1=int(input("Enter first number: "))
# num2=int(input("enter the second number"))

# print(num1>10 and num2>10)
# print(num1<5 or num2<5)
# print(not(num1>num2))

# age=int(input("enter your age: "))
# if age>=18:
#     print("your an adult")
# else:
#     print("your an minor")

# str=input("enter a string")
# print("a" in str)
# print("python" in str)


# a=3
# b=4
# print(a &b)
# print(a|b)
# print(a^b)
# print(a<<2)
# print(b>>1)

#popping the element in the list
items=["a","b","c","d"]
#print(items.pop(1))
print(items )
items.append("z")
print(items)

items.remove("c")
print(items)

#inseert the element at the specific index
items.insert(1,"x")
print(items)
items[0]="hello"
print(items)

#list slicing
print(items[1:4])
print(items[1:5:2])

print(8)
print(10,end="") #this is used to not to skip to the next line 
print(21)

word = "Python"
for char in word:
    print(char)

print(7 / 2) #/is a floor division ,if u take the 7 or 7.0 then output will be in decimsl only .to get the integer division .use // in the division ,this gives integer value 

name=""
if name:
    print(f"Hello,{name}")
else:
    print("hello,guest")