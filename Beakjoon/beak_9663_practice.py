N = int(input())
count=0
board=[0]*N


#Äı ³õ±â
def chess(n):
    global count
    if N==n:
        count=count+1
        return
    else:
        for i in range(N):
            board[n] = i
            if check(n):
                chess(n+1)
                

def check(n):
    for i in range(n):
        if board[n] == board[i] or abs(board[n]-board[i]) == abs(n-i):
            return False
        
    return True


chess(0)
print(count)