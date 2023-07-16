t=int(input())
count=1
for i in range(t):
    a,b,c=map(int,input().split())
    while c>a:
        c=c-a
        count=count+1
    print((c*100)+count)
    count=1
        