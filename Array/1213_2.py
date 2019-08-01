import sys
sys.stdin = open('1213.txt', 'rt', encoding='UTF-8')

for t in range(10):
    tc = input()
    target = input()
    letters = list(input())
    count = 0
    for i in range(len(letters)):
        if target in ''.join(letters[i:i+len(target)]):
            count += 1

    print('#{} {}'.format(tc, count))