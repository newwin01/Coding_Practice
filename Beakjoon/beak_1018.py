n, m = map(int,input().split())
board = []
minimum = []

for i in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        W=0
        B=0
        for k in range(i,i+8):
            for z in range(j,j+8):
                if (k+z) % 2 == 0:
                    if board[k][z]!='W': W+=1
                    if board[k][z]!='B': B+=1
                else:
                    if board[k][z]!='B': W+=1
                    if board[k][z]!='W': B+=1
        minimum.append(W)
        minimum.append(B)


print(min(minimum))        
