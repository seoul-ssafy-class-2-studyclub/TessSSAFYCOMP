'''
1209. [S/W 문제해결 기본] 2일차 - Sum
'''
import sys
sys.stdin = open('1209.txt', 'r')

## 각 행의 합의 최댓값
def msum(arr):
    pre_count_list = []
    for i in range(100):
        count = 0
        try:
            for ix in range(len(pre_count_list)):
                count += arr[i][ix] # 0 0 0 1 0 2 0 3 0 4
            pre_count_list.append(count)
        except:
            continue

    temp = pre_count_list[0]
    for i2 in range(1, len(pre_count_list)):
        if temp < pre_count_list[i2]:
            temp = pre_count_list[i2]

    row_board = []
    row_board.append(temp)
    print(row_board)
    temp2 = row_board[0]
    for i3 in range(1, len(row_board)):
        if temp2 < row_board[i3]:
            temp2 = row_board[i3]
    return temp2


for tc in range(10): # 100 x 100 의 보드판
    big_board = []
    for tb in range(100):
        #print(tb)
        small_board = list(map(int, input().split()))
        #print(len(small_board))
        big_board.append(small_board)

    #board완성
    #print(big_board)
    # 해당 보드에서 각 행의 합, 각 열의 합, 각 대각선의 합의 최댓값을 구한다.

    ## 각 행의 합의 최댓값
    ms = msum(big_board)


    print(ms)



