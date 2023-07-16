a,b,c=map(int,input().split())
day=(c-b)/(a-b)
if day%1==0:
    print(int(day))
else:
    print(int(day+1))