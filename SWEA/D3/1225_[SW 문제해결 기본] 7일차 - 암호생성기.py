T=10
for test_case in range(1,T+1):
    tc=int(input())
    data=list(map(int,input().split()))
    while True:
        if data[-1]==0: break
        for i in range(1,5):
            if data[-1]==0: break
            check=data.pop(0)
            check-=i
            data.append(check)

    print(f'#{test_case} ',end='')
    for i in data:
        print(i,end='')
    print()
        
