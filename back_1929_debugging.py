def Prime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
    return True

b=int(input())

for i in range(b):
    if Prime(i):
        print(i)