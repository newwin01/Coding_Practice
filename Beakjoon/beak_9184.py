import sys
input = sys.stdin.readline

dp = [ [ [0]*(21) for _ in range(21)] for _ in range(21)]

def w_compute(a_value, b_value, c_value):
    if a_value <= 0 or b_value <= 0 or c_value <= 0:
        return 1
    if a_value > 20 or b_value > 20 or c_value > 20:
        return w_compute(20, 20, 20)
    
    if dp[a_value][b_value][c_value]:
        return dp[a_value][b_value][c_value]
    
    if a_value < b_value and b_value < c_value:
        dp[a_value][b_value][c_value] = w_compute(a_value, b_value, c_value - 1) + w_compute(a_value, b_value - 1, c_value - 1) - w_compute(a_value, b_value - 1, c_value)
    else:
        dp[a_value][b_value][c_value] = w_compute(a_value - 1, b_value, c_value) +  w_compute(a_value - 1, b_value - 1, c_value) + w_compute(a_value - 1, b_value, c_value - 1) - w_compute(a_value - 1, b_value - 1, c_value - 1)
    
    return dp[a_value][b_value][c_value]

while 1:
    a_value, b_value, c_value = map(int, input().split(" "))
    if a_value == -1 and b_value == -1 and c_value == -1:
        break

    print("w({}, {}, {}) = {}".format(a_value, b_value, c_value, w_compute(a_value, b_value, c_value)))
