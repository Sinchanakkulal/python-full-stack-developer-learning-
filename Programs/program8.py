#write a program to solve the quadratic equation 
import math

a=int(input("enter the  coefficient of a :"))
b=int(input("enter the coefficient of b :"))
c=int(input("enter the coefficient of c :"))

descriminant=b**2-b*a*c

if descriminant>0:
    root1=(-b + math.sqrt(descriminant))/(2*a)
    root2=(-b - math.sqrt(descriminant))/(2*a)
    print(f"Root1 : {root1}")
    print(f"Root2 : {root2}")
elif descriminant==0:
    root=(-b * (2*a))
    print(f"Root :{root}")
else:
    real_part= -b/(2*a)
    imaginary_part =math.sqrt(abs(descriminant))/(2*a)
    print(f"Root1: {real_part}+{imaginary_part}i")
    print(f"Root2 : {real_part}-{imaginary_part}i")
