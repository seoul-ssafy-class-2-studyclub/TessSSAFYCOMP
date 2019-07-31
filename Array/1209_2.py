'''
1209. [S/W 문제해결 기본] 2일차 - Sum
'''
import sys
sys.stdin = open('1209.txt', 'r')

## 각 행의 합의 최댓값
def mmax(arr):
    temp = arr[0]
    for i2 in range(1, len(arr)): # 각 행들을 담은 합들중에 가장 큰 값을 찾는다.
        if temp < arr[i2]:
            temp = arr[i2]
    return temp

def msum(arr):
    count = 0
    for ix in arr:
        count += ix
    return count

for tc in range(10): # 100 x 100 의 보드판
    t = int(input())
    big_board = []
    sum_board = []
    d1, d2 = 0, 0
    for tb in range(100):
        small_board = list(map(int, input().split()))
        big_board.append(small_board)    # board 완성

    # 해당 보드에서 각 행의 *합*, 각 열의 *합*, 각 대각선의 *합*의 최댓값을 구한다.
    ## 각 행의 합의 최댓값
    for r in big_board:
        sum_board.append(msum(r))

    new_list = list(map(list, zip(*big_board)))  # 편하게 다루기 위해 세로줄을 가로줄로 바꿔줌
    for c in new_list:
        sum_board.append(msum(c))

    for ib in range(100):
        # 대각선의 sum_board
        d1 += big_board[ib][ib]
        d2 += new_list[ib][ib]
    sum_board.append(d1)
    sum_board.append(d2)

    final_max = mmax(sum_board)
    print('#{} {}'.format(t, final_max))




