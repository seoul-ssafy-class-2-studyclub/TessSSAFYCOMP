'''
1216. [S/W 문제해결 기본] 3일차 - 회문2


'''

import sys
sys.stdin = open('1216.txt', 'r')

a = ['정', '승', '원']

print(a[::-1]) # ['원', '승', '정']

for tc in range(int(input())): # 100 x 100 의 보드판
    big_board = []

    for tb in range(100):
        big_board.append(list(map(str, input())))

    #가로 판단용 보드 완성
    print(big_board)

    for te in range(100):
        len_board = []
        max_board = []
        count = 0
        for tr in range(98):
            temp = big_board[te][te:tr]
            reversed_temp = temp[::-1]
            if temp == reversed_temp:
                len_board.append(len(reversed_temp))

        print(len_board)




