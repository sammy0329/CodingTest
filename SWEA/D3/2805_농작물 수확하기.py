T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    a = [list(map(int, input())) for _ in range(N)]
    result = 0

    # s: 시작점, e: 끝점
    s, e = N // 2, N // 2
    for i in range(N):
        for j in range(s, e+1):
            result += a[i][j]
            
        # 행의 인덱스가 mid가 되기 전까지 s와e 사이 간격 늘리고 mid보다 커지면 둘 사이 간격을 줄임
        if i < N // 2:
            s -= 1
            e += 1
            
        else:
            s += 1
            e -= 1
        
    print(f'#{test_case} {result}')