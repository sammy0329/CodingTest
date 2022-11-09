T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    L,U,X=map(int,input().split())
    # L이상 U이하 현재 X만큼 운동.
    if L>X:
        result=L-X
    elif U<X:
        result=-1
    else:
        result=0
    print(f'#{test_case} {result}')
