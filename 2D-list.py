#1d list
numbers=[1,2,3,4,5]
for i in numbers:
    print(i)
print(numbers)
#2d list /matrix
even_odd_prime=[[2,4,6,8,10],[1,3,5,7,9],[2,3,5,7,11]]
print(even_odd_prime)
#looping through for loop
for i in range(0,len(even_odd_prime)):
    for j in range(0,len(even_odd_prime[0])):
        print(even_odd_prime[i][j],end=" ")
    print("\n")
#take an input from the 2d list and print the elements
rows=int(input("enter the number of the row: "))
col=int(input("enter the number of the column: "))
matrix=[]
for i in range(rows):
    temp=[]
    for j in range(col):
        x=int(input("enter the element for the matrix "))
        temp.append(x)
    matrix.append(temp)
print(matrix)
#addition and subtraction in a matrix/2D list
matrxA=[[1,2,3],[4,5,6]]
matrxB=[[7,8,9],[10,11,12]]
additionResult= [[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        additionResult[i][j]=matrxA[i][j] + matrxB[i][j]
        print(additionResult)
