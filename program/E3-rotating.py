import os
import numpy as np
import time

start = input()
os.system('cls')

n = 30
basis = np.matrix([[0 for i in range(n)] for i in range(n)])

l0 = [8,8,8,8,8,8,8,8,8,8]
l1 = [8,8,8,8,8,8,8,8,8,8]
l2 = [8,8,1,1,1,1,1,1,1,1]
l3 = [8,8,1,1,1,1,1,1,1,1]
l4 = [8,8,8,8,8,8,8,8,8,8]
l5 = [8,8,8,8,8,8,8,8,8,8]
l6 = [8,8,1,1,1,1,1,1,1,1]
l7 = [8,8,1,1,1,1,1,1,1,1]
l8 = [8,8,8,8,8,8,8,8,8,8]
l9 = [8,8,8,8,8,8,8,8,8,8]
E = np.matrix([l0,l1,l2,l3,l4,l5,l6,l7,l8,l9])

for i in range(n-14):
    for x in range(n):
        for y in range(n):
            basis[x,y] = 1
    basis[2:12,i+2:i+12] = E
    print(basis)
    time.sleep(0.15)
    os.system('cls')

E = E.T
for i in range(n-14):
    for x in range(n):
        for y in range(n):
            basis[x,y] = 1
    basis[i+2:i+12,18:28] = E
    print(basis)
    time.sleep(0.15)
    os.system('cls')

l2.reverse()
l3.reverse()
l6.reverse()
l7.reverse()
E = np.matrix([l0,l1,l2,l3,l4,l5,l6,l7,l8,l9])

for i in range(n-14):
    for x in range(n):
        for y in range(n):
            basis[x,y] = 1
    basis[18:28,18-i:28-i] = E
    print(basis)
    time.sleep(0.15)
    os.system('cls')

E = E.T
for i in range(n-14):
    for x in range(n):
        for y in range(n):
            basis[x,y] = 1
    basis[18-i:28-i,2:12] = E
    print(basis)
    time.sleep(0.15)
    os.system('cls')


end = input()