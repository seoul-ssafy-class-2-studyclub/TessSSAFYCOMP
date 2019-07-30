''' max()함수 미사용ver '''

import sys
sys.stdin = open('input.txt', 'r')

def max(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        if temp < arr[i]:
            temp = arr[i]
    return temp

for t in range(10):
    B = int(input())
    a = list(map(int, input().split()))
    c = []
    for i in range(B-4):
        ax = max([a[i], a[i+1],  a[i+3], a[i+4]])
        if a[i] < a[i+2] and a[i+1] < a[i+2]:
            if a[i+3] < a[i+2] and a[i+4] < a[i+2]:
                c.append(a[i+2] - ax)
    s = sum(c)
    print('#{} {}'.format(t+1, s))
