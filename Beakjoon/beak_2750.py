N=int(input())
a=[]
for i in range(N):
    a.append(int(input()))

for i in range(N):
    for j in range(N):
        if a[i]<a[j] :
            tmp = a[j]
            a[j]=a[i]
            a[i] = tmp
for i in range (N):
    print(a[i])