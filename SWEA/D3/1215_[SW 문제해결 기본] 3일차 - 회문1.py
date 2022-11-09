# https://blackon29.tistory.com/63 정리

T = 10

def rotated(a):
    n = len(a)
    m = len(a[0])

    result = [[0]* n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

for test_case in range(1, T+1):

    p = int(input())
    N = 8
    cnt = 0
    dataset = [list(input()) for _ in range(N)]
    dataset_reverse=rotated(dataset)
    

    for i in range(0, N):
        for j in range(0, N-p+1):
            if dataset[i][j:j+p] == dataset[i][j:j+p][::-1]:
                cnt += 1
            if dataset_reverse[i][j:j+p] == dataset_reverse[i][j:j+p][::-1]:
                cnt += 1



    print(f'#{test_case} {cnt}')
    
