'''
1209. [S/W 문제해결 기본] 2일차 - Sum
'''
import sys
sys.stdin = open('1209.txt', 'r')

## 각 행의 합의 최댓값
def row_max(arr):
    pre_count_list = []
    for i in range(100):
        count = 0
        try:
            for ix in range(len(arr)):
                count += arr[i][ix] # 0 0 0 1 0 2 0 3 0 4
            pre_count_list.append(count) # 각행의 합을 pre_count_list에 담는다.
        except:
            continue

    # 각 행들을 담은 합들중에 가장 큰 값을 찾는다.
    temp = pre_count_list[0]
    for i2 in range(1, len(pre_count_list)):
        if temp < pre_count_list[i2]:
            temp = pre_count_list[i2]
    '''
            final_row_board.append(row_board[-1])
    
    temp2 = final_row_board[0]
    for i3 in range(1, len(final_row_board)):
        if temp2 < final_row_board[i3]:
            temp2 = final_row_board[i3]
            real_final_row_board.append(temp2)
            
    print(real_final_row_board)
    final_temp2 = real_final_row_board[-1]
    '''
    #10개 tc들의 temp 였음
    return temp

def columm_max(arr):
    new_list = list(map(list, zip(arr)))
    print(len(new_list)) #100으로 잘 zip됨
    #zip으로 묶어서 열을 행으로 만든다.

    pre_count_list = []
    for i in range(100):
        count = 0
        try:
            for ix in range(100):
                count += new_list[i][ix] # 0 0 0 1 0 2 0 3 0 4
            pre_count_list.append(count) # 각행의 합을 pre_count_list에 담는다.
        except:
            continue
    # 각 행들을 담은 합들중에 가장 큰 값을 찾는다.

    print(pre_count_list)

    temp = pre_count_list[0]
    for i2 in range(1, len(pre_count_list)):
        if temp < pre_count_list[i2]:
            temp = pre_count_list[i2]
    return temp


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
    rm = row_max(big_board) #1의 1541
    print(rm)

    cm = columm_max(big_board)
    print(cm)
