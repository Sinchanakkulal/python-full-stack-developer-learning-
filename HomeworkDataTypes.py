a=5
afloat=float(a)
print(type(afloat))

aint=int(afloat)
print(type(aint))
astring="100"
aSint=int(astring)
print(type(aSint))

sub=[1,2,3,4,5]
for i in sub:
    print(i)

Student={
    "name":"sinchana",
    "age":21,
    "College":"Mite"
}
print(Student["age"])

tup=(1,2,3,"Hello")
# print("trying to midofy the tuble")
# tup[0]=5
print(tup)
# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)

for i in range(5):
    pass

for i in range(1,3):
    for j in range(1,2):
        print(i,j)

#print the numbers from 1 to 100
for i in range(1,101):
    print(i)

#print the even number from 1 to 50
for i in range(1,51):
    if i%2==0:
        print(i)

print("print the multiplication table of a number ")
num=input("enter a number:")
for i in range(1,11):
    print(f"{num} x {i} = {int(num)*i}")

#print the even number
for i in range(1,51):
    if i%2==0:
        print(i)
    else:
        continue