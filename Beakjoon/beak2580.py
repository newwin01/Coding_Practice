#map 생성, 0 찾기
import numbers


sudoku_map = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i,j) for i in range(9) for j in range(9) if sudoku_map[i][j]==0]


#넣을 수 있는 숫자 찾기
def exist(i,j):
    number = [1,2,3,4,5,6,7,8,9]


    for k in range (9):
        if sudoku_map[i][k] in number:
            number.remove(sudoku_map[i][k])
        
        if sudoku_map[k][j] in number:
            number.remove(sudoku_map[k][j])
        
    
    i = int(i/3)
    j = int(j/3)

    for l in range(i*3,(i+1)*3):
        for m in range(j*3,(j+1)*3):
            if sudoku_map[l][m] in number:
                number.remove(sudoku_map[l][m])
    return number


def solution(n):
    if n == len(zeros):
        for pr in sudoku_map:
            print(*pr)
        exit(0)

    else:
        (i,j) = zeros[n]
        number = exist(i,j)

        for x in number:
            sudoku_map[i][j] = x
            solution(n+1)
            sudoku_map[i][j] = 0


solution(0)