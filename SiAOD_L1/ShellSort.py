from random import randint
import time 
t0 = time.clock()

"""
Method arrays
"""

def BildArray(n, m):
    c = [[randint(100, 999) for j in range(m)] for i in range(n)]
    
    d = [0]*m
    
    return c, d

"""
Method sort
"""
def shell(array):
    inc = len(array) // 2
    while inc:
        for i, el in enumerate(array):
            while i >= inc and array[i - inc] > el:
                array[i] = array[i - inc]
                i -= inc
            array[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)


"""
Body program
"""
n, m = 1000, 1000

a, b = BildArray(n, m)
t = 0
while t != m:
    for j in range(n):
        b[j] = a[t][j]
    shell( b )
    for j in range ( len(b) ): 
        print ( "{:4d}".format(b[j]), end = "" )
    print()
    t += 1

t1 = time.clock() - t0
print("Time elapsed: ", t1 - t0)