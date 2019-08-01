import sys
sys.stdin = open('1213.txt', 'rt', encoding='UTF-8')


tc = input() # tc = 1
target = input() # ti
letters = list(input())
print(tc, target, letters)

count = 0

print(str(target))
for i in range(len(letters)):
    # ['t', 'i']
    if target in ''.join(letters[i:len(target)]):
        print('if문이 True이다')
        count += 1

print(count)