num=int(input())
num_arr=[]
for i in str(num):
    num_arr.append(int(i))

num_arr.sort(reverse=True)

for i in num_arr:
    print(i,end='')