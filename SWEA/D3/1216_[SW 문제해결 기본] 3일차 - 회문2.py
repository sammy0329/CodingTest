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
    tc=int(input())
    N = 100
    dataset = [list(input()) for _ in range(N)]
    dataset_reverse=rotated(dataset)
    
    solution=1
    for i in range(N):
        for p in range(2,N+1):
            for j in range(0, N-p+1):
                if dataset[i][j:j+p] == dataset[i][j:j+p][::-1]:                
                    if solution<p:
                        solution=p
                    break
                
                if dataset_reverse[i][j:j+p] == dataset_reverse[i][j:j+p][::-1]:
                    if solution<p:
                            solution=p
                    break

    print(f'#{test_case} {solution}')

