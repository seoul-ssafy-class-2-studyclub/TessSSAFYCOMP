def my_max(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        if temp < arr[i]:
            temp = arr[i]
    return temp

def my_min(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        if temp > arr[i]:
            temp = arr[i]
    return temp

for T in range(int(input())):
    N = int(input())
    aj = list(map(int, input().split()))
    result =  my_max(aj) - my_min(aj)
    print('#{} {}'.format(T+1, result))