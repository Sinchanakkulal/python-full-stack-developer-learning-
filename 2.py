#to find the index of the character 't' in the string "sinchana"
name="sinchana"
print(name[3])
print(name[2:5])
print(name[2:])
print(name[2:5:2])  # slicing with step:(start:end:step)
#from the backwards also ,we can print the character by using -1,-2 etc

#we can use escape sequence(\n) in the string with (\t)
s="sinchana\npython"
print(s)

x=None
print(type(x))

a=10    
b=20
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)

#logicaloperator
print(a<b and a!=b)
print(a<b or a==b)
print(not(a<b))

#membership operator:to check whether this is a member of that grp
list=[1,2,3,4]
my_string="sinchana"
print("i" in my_string)
print("z" in my_string)
print(5 in list)

