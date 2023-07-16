import math

def Prime(num):
    n=int(math.sqrt(num))
    if num==1:
        return False
    else:
        for i in range(2, n+1):
            if num%i == 0:
                return False
    return True

a,b=map(int,input().split())

for i in range(a,b+1):
    if Prime(i):
        print(i)