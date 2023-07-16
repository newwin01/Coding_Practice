a=int(input())
count=0
for i in range(a):
    a=a-count
    count=count+1
    if count>=a:
        if count%2!=0:
            print(str((count-a+1))+"/"+str(a))
        else:
            print(str(a)+"/"+str((count-a+1)))
        break