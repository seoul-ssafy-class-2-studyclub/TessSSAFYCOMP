'''
row <= 1000
height <= 255
맨 왼쪽 두칸과
오른쪽 두칸에는 건물이 지어지지 않는다.

T = 10

100

각 층이 주어진다
100이 가로길이
가장 높은 세로를 찾아서 그만큼의 board를 만든다
0 0 225 214 82 73 241 233 179 219 135 62 36 13 6 71 179 77 67 139 31 90 9 37 93 203 150 69 19 137 28 174 32 80 64 54 18 0 158 73 173 20 0 102 107 48 50 161 246 145 225 31 0 153 185 157 44 126 153 233 0 201 83 103 191 0 45 0 131 87 97 105 97 209 157 22 0 29 132 74 2 232 44 203 0 51 0 244 212 212 89 53 50 244 207 144 72 143 0 0


#1

691
'''


T = 1
B = 100
a = [0, 0, 225, 214, 82, 73, 241, 233, 179, 219, 135, 62, 36, 13, 6, 71, 179, 77, 67, 139, 31, 90, 9, 37, 93, 203, 150, 69, 19, 137, 28, 174, 32, 80, 64, 54, 18, 0, 158, 73, 173, 20, 0, 102, 107, 48, 50, 161, 246, 145, 225, 31, 0, 153, 185, 157, 44, 126, 153, 233, 0, 201, 83, 103, 191, 0, 45, 0, 131, 87, 97, 105, 97, 209, 157, 22, 0, 29, 132, 74, 2, 232, 44, 203, 0, 51, 0, 244, 212, 212, 89, 53, 50, 244, 207, 144, 72, 143, 0, 0]   #list(map(int,input().split()))

#height = max(a) #246

#board = [[0]*B for i in range(height)]  # 가로 100만큼의 246 세로 보드 완성
#print(len(board)) #246
#print(len(a)) #100개

check_ok = [1, 1] #1이 조망권 확보 2가 조망권 불확보

for t in range(T):
    check_board = []
    try:
        for x in range(2):  # 총 두번만 돌자
            for i in range(B): # 0~99

                if a[i] < a[i+2] and a[i+1] < a[i+2]:  # 0 < 225  0 < 225, 1
                    check_board.append(1)
                    continue
                else:
                    check_board.append(2)
                    continue

            for i in range(B):
                if a[i+3] < a[i+2] and a[i+4] < a[i+2]: # 214 < 225 82 < 225, 2
                    check_board.append(1)
                    continue
                else:
                    check_board.append(2)
                    continue
    except IndexError:
        break

    finally:
        print(check_board)  # [1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 2, 2, 2, 2]
        count = 0
        for x in range(0, len(check_board), 2):
            try:
                if [check_board[x], check_board[x+1]] ==  check_ok:
                    count += 1
            except:
                break

        print(count)

print(list(range(0,100,2)))
#print(len(a)) # 24
#n = [
# 1, 2,
#  2, 2,
#  1, 2,
#  2, 2,
#  2, 2,
#  2, 2,
#  2, 1,
# 1, 2,
#  2, 1
# ] # 18
#print(len(n))
