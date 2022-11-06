T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    current_loc=0
    current_speed=0
    for i in range(n):
        data=list(map(int,input().split()))
        if data[0]==1:
            current_speed+=data[1]
            current_loc+=current_speed
        elif data[0]==2:
 
            current_speed-=data[1]
            if current_speed<0:
                current_speed=0
            current_loc+=current_speed
        else:
            current_loc+=current_speed
    print(f'#{test_case} {current_loc}')