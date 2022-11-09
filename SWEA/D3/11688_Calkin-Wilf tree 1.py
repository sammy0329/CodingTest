

T = int(input())
for test_case in range(1, T + 1):
    result=[1,1]
    
    data=list(input())
    
    for check in data:
        if check=='L':
            result[1]=result[0]+result[1]
        elif check=='R':
            result[0]=result[0]+result[1]
    print(f'#{test_case} {result[0]} {result[1]}')
