import sys
count=int(sys.stdin.readline())
coor_arr=[]
for i in range(count):
    coor_arr.append(list(map(int, sys.stdin.readline().split())))

coor_arr.sort(key=lambda x:(x[1],x[0]))
    
for i in range(count):
    print(coor_arr[i][0],coor_arr[i][1])

