import sys

queue = []
num_op = int(sys.stdin.readline())
#front, rear
front = 0
for i in range(num_op):
    op = sys.stdin.readline()
    strings = op.split() #array of string
    if strings[0] == "push":
       value = strings[1]
       queue.append(value)

    elif strings[0] == "pop":
        if len(queue) <= front:
            print(-1)
        else:
            print(queue[front])
            front +=1
    
    elif strings[0] == "size":
        print(len(queue)-front)

    elif strings[0] == "empty":
        if len(queue) == front:
            print(1)
        else: 
            print(0)
    
    elif strings[0] == "front": 
        if len(queue) <= front:
            print(-1)
        else:
            print(queue[front])
    
    elif strings[0] == "back":
        if len(queue) <= front:
            print(-1)
        else:
            print(queue[-1])
