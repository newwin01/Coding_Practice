N=input()
M=int(N)
Val=int(N)
torf=0
for i in N:
    M=M-9
for j in range(M,Val+1):
    final_val=0
    num=j
    while(num>0):
        final_val=final_val+(num%10)
        num=num//10
    if((final_val+j)==Val):
        print(j)
        torf=1
        break
if torf==0:
    print(0)