T = int(input())
for t in range(1, T + 1):
    MAX_NUM = 10
    cards = int(input())
    A = list(map(int, input()))
    count = [0]*(MAX_NUM+1)
    for i in range(0, cards):
        count[A[i]] += 1

    num = count[0]
    for id in range(len(count)):
        if num <= count[id-1]: # 0, 1, 2, 3, 4,
            num = count[id-1]  # 2
            if num == count[id-1]:
                x = len(count[0: id-1])


    print('#{} {} {}'.format(t, x, num))