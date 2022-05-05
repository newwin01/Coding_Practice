
N = input()
count=int(0)
board=[]

def chess(n):
    if(N==n):
        global count
        count=count+1
    else:
        for i in range(N):
            for j in range(N):
                board[i][j]=1


def check(n):
    for i in range(n):
        for j in range(n):
            if(board[i][j]==1):
                return False

            