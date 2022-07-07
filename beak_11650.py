import sys
count=int(sys.stdin.readline())
coor_arr=[]
for i in range(count):
    coor_arr.append(list(map(int, sys.stdin.readline().split())))

coor_arr.sort()
    
for i in range(count):
    print(coor_arr[i][0],coor_arr[i][1])