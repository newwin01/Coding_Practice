import sys

sudoku_map = []
zeros = []


for i in range(9):
    sudoku_map.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if sudoku_map[i][j]==0:
            zeros.append((i,j))

def checkRow(i,n):
    for k in range(9):
        if n == sudoku_map[i][k]:
            return False
    return True


def checkCol(j,n):
    for k in range (9):
        if n == sudoku_map[k][j]:
            return False
    return True

def checkBox(i,j,n):
    i = i//3*3
    j = j//3*3
    for x in range(3):
        for y in range(3):
            if n == sudoku_map[x+i][y+j]:
                return False
    return True

def solution(n):
    if n == len(zeros):
        for pr in sudoku_map:
            print(*pr)
        exit(0)


    for i in range(1,10):
        x = zeros[n][0]
        y = zeros[n][1]

        if checkRow(x,i) and checkCol(y,i) and checkBox(x,y,i):
            sudoku_map[x][y] = i
            solution(n+1)
            sudoku_map[x][y] = 0


solution(0)