import sys
sys.stdin = open('1961.txt', 'r')

for tc in range(int(input())):
    two = []
    r1, r2, r3 = ([], [], [])

    B = int(input())
    for b in range(B):
        one_dimension_board = list(map(str, input().split()))
        two.append(one_dimension_board)

    two = list(map(list, zip(*two)))
    for b1 in range(B):
        two[b1][::-1]
        frist_result = ''.join(two[b1][::-1])
        r1.append(frist_result)

    for b3 in range(B):
        two[b3]
        third_result = ''.join(two[b3])
        r3.append(third_result)
        
    second_two = list(map(list, zip(*two)))
    for b2 in range(B):
        second_two[b2][::-1]
        second_result = ''.join(second_two[b2][::-1])
        r2.append(second_result)

    r2 = r2[::-1]
    r3 = r3[::-1]
    
    print('#{}'.format(tc+1, end=''))
    for b4 in range(B):
        print('{} {} {}'.format(r1[b4], r2[b4], r3[b4]))

'''
#1
741 987 369
852 654 258
963 321 147
'''