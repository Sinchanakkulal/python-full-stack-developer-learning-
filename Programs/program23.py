#print the number from 5 to 1 through recursion 

def printNumb(n):
    if n==0:
        return 
    print(n)
    printNumb(n-1)

n=5
printNumb(n)