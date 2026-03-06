"""
A parking lot in a mall has RxC number of parking spaces. Each parking space will either be  empty(0) or full(1). The status (0/1) of a parking space is represented as the element of the matrix. The task is to find index of the prpeinzta row(R) in the parking lot that has the most of the parking spaces full(1).

Note :
RxC- Size of the matrix
Elements of the matrix M should be only 0 or 1.

Example 1:
Input :
3   -> Value of R(row)
3    -> value of C(column)
[0 1 0 1 1 0 1 1 1] -> Elements of the array M[R][C] where each element is separated by new line.
Output :
3  -> Row 3 has maximum number of 1’s

Example 2:
input :
4 -> Value of R(row)
3 -> Value of C(column)
[0 1 0 1 1 0 1 0 1 1 1 1] -> Elements of the array M[R][C]
Output :
4  -> Row 4 has maximum number of 1’s
"""
R = int(input("enter the row size: "))
C = int(input("enter the column size: "))
matrix = [[0] * C for _ in range(R)]
for i in range(0,R):
    for j in range(0,C):
        matrix[i][j] = int(input(f"enter element at position [{i}][{j}]: "))

max = 0
row_indecs = -1
for i in range(R):
    count = 0
    for j in range(C):
        if matrix[i][j] == 1:
            count +=1
    if count > max:
        max = count
        row_indecs = i

print(f"row with maximum index is {row_indecs+1}")
        
            