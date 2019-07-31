import sys
sys.stdin = open('1221.txt', 'r')

'''
GNS

'''
number_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(int(input())):
    tcc, N = tuple(map(str, input().split())) #  #1 7041
    N = int(N) # 7041
    letter_list = list(map(str, input().split()))
    temp_dict = {}
    for letter in number_list:
        temp_dict[letter] = letter_list.count(letter) #{'FOR': 679, 'NIN': 704, 'EGT': 724, 'SIX': 674, 'THR': 734, 'TWO':719, 'ZRO': 700, 'ONE': 716, 'FIV': 737, 'SVN': 654}
    temp_list = []
    for letter in number_list:
        if letter in temp_dict:
            temp_list.append(temp_dict[letter])
    # print(temp_list) #[700, 716, 719, 734, 679, 737, 674, 654, 724, 704] number_list에 맞게 순서대로 정렬되었다.
    # list 처럼 dictionary 정렬
    # 그다음에 곱해서 새로운 리스트에 append
    print('')
    print('{}'.format(tcc))
    for i in range(10):
        for ix in range(temp_list[i]):
            print(number_list[i], end=" ")
