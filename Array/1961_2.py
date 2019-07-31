import sys
sys.stdin = open('1961.txt', 'r')

for tc in range(int(input())):
    two = []
    r1, r2, r3 = ([], [], [])
    B = int(input())
    for b in range(B):
        two.append(list(map(str, input().split())))
    two = list(map(list, zip(*two)))
    for b1 in range(B):
        r1.append(''.join(two[b1][::-1]))
        r3.append(''.join(two[b1]))
    s_two = list(map(list, zip(*two)))
    for b2 in range(B):
        r2.append(''.join(s_two[b2][::-1]))
    r2, r3 = r2[::-1], r3[::-1]
    print('#{}'.format(tc+1, end=''))
    for b4 in range(B):
        print('{} {} {}'.format(r1[b4], r2[b4], r3[b4]))

'''
#1
741 987 369
852 654 258
963 321 147
'''