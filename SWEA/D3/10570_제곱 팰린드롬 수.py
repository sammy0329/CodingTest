from math import * 

T = int(input())
for test_case in range(1, T + 1):
    a,b=map(int,input().split())
    cnt=0

    for num in range(a,b+1):
        check=str(num)
        
        if sqrt(num)==int(sqrt(num)):
            check_sqrt=str(int(sqrt(num)))
        else:
            continue

        if check[::-1]==check and check_sqrt[::-1]==check_sqrt:
            cnt+=1
    print(f'#{test_case} {cnt}')    
