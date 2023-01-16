import sys

stack = []
num_op = int(sys.stdin.readline())

for i in range(num_op):
    op = int(sys.stdin.readline())

    if(op==0):
        stack.pop()

    else:
        stack.append(op)

sum = sum(stack)

print(sum)