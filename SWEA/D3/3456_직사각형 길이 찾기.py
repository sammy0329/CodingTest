T=int(input())

for test_case in range(1,T+1):
    
    data=list(map(int,input().split()))
    check=set(data)
    result=0
    
    for j in check:
        if data.count(j)!=2:
            result=j
            break
        
    print(f'#{test_case} {result}')