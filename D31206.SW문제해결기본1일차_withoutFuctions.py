def max(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        if temp < arr[i]:
            temp = arr[i]
    return temp


for t in range(10):
    B = int(input())
    a = list(map(int, input().split()))
    check_board = []
    for i in range(B-4):
        max_b = max([a[i], a[i+1],  a[i+3], a[i+4]])
        if a[i] < a[i+2] and a[i+1] < a[i+2]:
            if a[i+3] < a[i+2] and a[i+4] < a[i+2]:
                result = a[i+2] - max_b
                check_board.append(result)
    sum_result = sum(check_board)
    print('#{} {}'.format(t+1, sum_result))
