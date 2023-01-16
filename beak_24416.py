def fib_rec(n):
    if(n==1 or n==2):
        return 1
    else:
        return (fib_rec(n-1)+fib_rec(n-2))

def fib_dy(n):
    fib = [0]*(n+1)
    fib[1] = 1
    fib[2] = 1
    count = 0
    for i in range(3, n+1):
        count = count+1
        fib[i] = fib[i-1] + fib[i-2]
    return count

n = int(input())
print(fib_rec(n),fib_dy(n))