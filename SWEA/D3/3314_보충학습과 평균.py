T = int(input())

for test_case in range(1, T + 1):
    scores=list(map(int,input().split()))
    result=0
    for check in scores:
        if check<=40:
            result+=40
        else:
            result+=check
    print(f'#{test_case} {result//5}')