import sys
sys.stdin = open('1961.txt', 'r')

'''
10
3
1 2 3
4 5 6
7 8 9

'''
for tc in range(int(input())):
    two_dimension_board = []
    result_board1 = []
    result_board2 = []
    result_board3 = []

    B = int(input())
    for b in range(B):
        one_dimension_board = list(map(str, input().split()))
        two_dimension_board.append(one_dimension_board)

    
    two_dimension_board = list(map(list, zip(*two_dimension_board)))
    # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    
    # 90도
    for b1 in range(B):
        two_dimension_board[b1][::-1]
        # [7, 4, 1] [8, 5, 2] [9, 6, 3]
        # 돌린거를 합쳐서 90 리스트에 append
        frist_result = ''.join(two_dimension_board[b1][::-1]) #string값 squence join 가능
        result_board1.append(frist_result)

    #two_dimension_board한번더 zip하고 ::-1
    #180도
    second_two_dimension_board = list(map(list, zip(*two_dimension_board)))

    for b2 in range(B):
        second_two_dimension_board[b2][::-1]
        second_result = ''.join(second_two_dimension_board[b2][::-1])
        result_board2.append(second_result)

    #270도 다 구함
    #270은 중복되므로 나중에 수정
    third_two_dimension_board = list(map(list, zip(*second_two_dimension_board)))
    for b3 in range(B):
        third_two_dimension_board[b3]
        third_result = ''.join(third_two_dimension_board[b3])
        result_board3.append(third_result)
    
    result_board1
    result_board2 = result_board2[::-1]
    result_board3 = result_board3[::-1]
    
    print('#{}'.format(tc+1, end=''))
    for b4 in range(B):
        print('{} {} {}'.format(result_board1[b4], result_board2[b4], result_board3[b4]))