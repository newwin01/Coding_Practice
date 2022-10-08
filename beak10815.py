from http.client import NOT_FOUND
import sys

N = int(sys.stdin.readline())
array1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
array2 = list(map(int, sys.stdin.readline().split()))

_dict = {}  # 속도는 dictionary!
for i in range(N):
    _dict[array1[i]] = 0  # 아무 숫자로 mapping

for j in range(M):
    if array2[j] not in _dict:
        print(0, end=' ')
    else:
        print(1, end=' ')

# or use binary search

array1.sort()
def binsearch(array, target, start, end):
    while start<=end:
        middle = (start+end)//2
        if array[middle]==target:
            return middle
        elif array[middle]>target:
            end=middle-1
        else:
            start=middle+1
    return NOT_FOUND