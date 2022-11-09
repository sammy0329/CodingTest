T=10
for test_case in range(1,T+1):
    len=int(input())
    magnets=[list(map(int,input().split())) for _ in range(len)]
    cnt=0
    
    for i in range(len):
        check=False
        for j in range(len):
            if magnets[j][i]==1:
                check=True
            elif magnets[j][i]==2 and check:
                cnt+=1
                check=False

    print(f'#{test_case} {cnt}')