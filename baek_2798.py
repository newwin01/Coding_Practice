n,m=map(int,input().split())
arr=list(map(int,input().split()))
final_val=0;
for i in range(n):
    for  j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]+arr[j]+arr[k]>m:
                continue
            else:
                if final_val<arr[i]+arr[j]+arr[k]:
                    final_val=arr[i]+arr[j]+arr[k]
print(final_val)