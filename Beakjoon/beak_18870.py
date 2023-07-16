N=int(input())
coordinate = list(map(int,input().split()))
    
sorted_coordinate = sorted(list(set(coordinate)))#중복된 수 제거
print(sorted_coordinate)
sorted_coordinate = {sorted_coordinate[i]: i for i in range(len(sorted_coordinate))}
print(sorted_coordinate)
for i in coordinate:
    print(sorted_coordinate[i], end=' ')