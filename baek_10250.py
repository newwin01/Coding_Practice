t=int(input())
count=1
for i in range(t):
    a,b,c=map(int,input().split())
    floor=c%a
    room=c//a+1
    if floor==0:
        floor=a
        room=room-1
    print(floor*100+room)
        