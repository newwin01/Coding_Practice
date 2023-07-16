#counting sort
import sys
N=int(sys.stdin.readline())
MAX_NUM=10000+1
max_arr=[0]*(MAX_NUM)
for i in range(N):
    num=int(sys.stdin.readline())
    max_arr[num] = max_arr[num]+1
for i in range (MAX_NUM):
    if max_arr[i]!=0:
        for j in range(max_arr[i]):
            print(i)