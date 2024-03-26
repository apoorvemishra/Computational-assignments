#Computational Physics Assignment 1


import numpy as np
import time




#Question 11
print("Question 11 solutions")
A1 = [[3,-1,1],[3,6,2],[3,3,7]]
b1 = [1,0,4]
print(np.linalg.solve(A1,b1))

A2 = [[10,-1,0],[-1,10,-2],[0,-2,10]]
b2 = [9,7,6]
print(np.linalg.solve(A2,b2))

A3 = [[10,5,0,0],[5,10,-4,0],[0,-4,8,-1],[0,0,-1,5]]
b3 = [6,25,-11,-11]
print(np.linalg.solve(A3,b3))

A4 = [[4,1,1,0,1],[-1,-3,1,1,0],[2,1,5,-1,-1],[-1,-1,-1,4,0],[0,2,-1,1,4]]
b4 = [6,6,6,6,6]
print(np.linalg.solve(A4,b4))
print('***************************************************')


#Question 17

print("\n\nQuestion 17 solutions")
A = [[5,-2],[-2,8]]
B = np.linalg.qr(A)
print("Q matrix = ")
print(B[0])
print("R matrix = ")
print(B[1])
print("\nLets calculate eigen values of A using QR decomposition")
while A[0][1]>0.01 or A[0][1]<-0.01:
    B = np.linalg.qr(A)
    A = np.dot(B[1],B[0])
print(A)
print('\nAs we can see, diagonal elements of this matrix approaches eigen values and off diagonal elements are approaching 0')
c = np.linalg.eigh(A)
print("Eigen value of matrix using linalg.eigh are")
print(c[0])
print('***************************************************')




#Question 18
print("\n\nQuestion 18 solutions")
A = [[2,-1,0],[-1,2,-1],[0,-1,2]]
x = np.random.random_sample(size = 3)
An = []
y = np.random.random_sample(size = 3)
z = 2
while z<0.99 or z>1.01:
    x = np.dot(A,x)
    An.append(np.dot(x,y))
    if len(An)>2:
        z = (An[2]*An[0])/(An[1]*An[1])
        An.pop(0)

print('Dominent eigne value for A is = ')
print(An[1]/An[0])
print('***************************************************')

    

#Question 19
print("\n\nQuestion 19 solutions")
A = []
A.append([[2,1],[1,0]])
A.append([[2,1],[1,0],[0,1]])
A.append([
    [2, 1],
    [-1, 1],
    [1, 1],
    [2, -1]
])
A.append([
    [1, 1, 0],
    [-1, 0, 1],
    [0, 1, -1],
    [1, 1, -1]
])
A.append([
    [1, 1, 0],
    [-1, 0, 1],
    [0, 1, -1],
    [1, 1, -1]
])
A.append([
    [0, 1, 1],
    [0, 1, 0],
    [1, 1, 0],
    [0, 1, 0],
    [1, 0, 1]
])

print('''For each matrix, I am printing :- \n
      1. time taken to calculate SVD\n
      2. U matrix\n
      3. V matrix\n
      4. S matrix as just its diagonal elements\n
      5. Squars of each element of diagonal matrix S\n
      6. A transpose A martix eigen values\n
finally if entry 5 and 6 are same then my calculations are correct\n''')


for i in range(6):
    print('%dst Matrix' % (i+1))
    ti = time.time()
    svd = np.linalg.svd(A[i])
    tf = time.time()
    print("1. %f seconds" % (tf-ti))
    print("2. ", end="")
    print(svd[0])
    print("3. ", end="")
    print(svd[2])
    print("4. ", end="")
    svd[1].sort()
    print(svd[1])
    print("5. ", end="")
    print(svd[1]**2)
    print("6. ", end="")
    ta = np.dot(np.transpose(A[i]),A[i])
    print(np.linalg.eigh(ta)[0])
    print('\n')
print('***************************************************')













