print("count the sum of numbers in a list")
nums=[1,2]
sum=0
for i in nums:
    sum+=i
print(sum)

print("print the stars in pyramid")
num=4
def half_pyramid(n):
    if n>0:
        half_pyramid(n-1)
        print("* "*n)

half_pyramid(num)
    
print("full pyramid")
def full_pyramid(n):
    for i in range(1,n+1):
        for j in range(0,n-i):
            print(" ",end="")
        for k in range(1,2*i):
            print("*",end="")
        print()

full_pyramid(5)

