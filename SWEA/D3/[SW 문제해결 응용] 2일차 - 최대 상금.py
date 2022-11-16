# 도전중..

def sel_sort(arr,n):
    

    if n>len(arr):
    for i in range(0, n - 1):

        max_idx = i # 최솟값(min) 대신 최댓값(max)을 찾아야 함

        for j in range(i + 1, n):

            if arr[j] > arr[max_idx]: # 부등호 방향 뒤집기

                max_idx = j

        arr[i], arr[max_idx] = arr[max_idx], arr[i]

 

arr,n = map(int,input().split())
arr_=list(str(arr))
arr=list()

for i in range(len(arr_)):
    arr.append(int(arr_[i]))

sel_sort(arr,n+1)

print(arr)