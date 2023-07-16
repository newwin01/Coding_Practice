N=int(input())
Member_list=[]
for i in range(N):
    Member_list.append(list(input().split()))
    
Member_list.sort(key=lambda x:int(x[0]))
for i in range(N):
    print(Member_list[i][0],Member_list[i][1])