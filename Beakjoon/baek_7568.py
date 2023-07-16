N=int(input())
arr=[]
for i in range(N):
    val1,val2=map(int,input().split())
    arr.append((val1,val2))
for i in arr:
    rank=1
    for j in arr:
        if i[0]<j[0] and i[1]<j[1]:
                    rank=rank+1
    print(rank,end=' ')