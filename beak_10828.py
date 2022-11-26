import sys

stack = []
num_op = int(sys.stdin.readline())

for i in range(num_op):
    op = sys.stdin.readline()
    strings = op.split()
    if strings[0] == "push":
       value = strings[1]
       stack.append(value)

    elif strings[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    
    elif strings[0] == "size":
        print(len(stack))

    elif strings[0] == "empty":
        if len(stack) == 0:
            print(1)
        else: 
            print(0)
    
    elif strings[0] == "top": 
        if len(stack) == 0:
            print(-1)

        else:
            print(stack[-1])
