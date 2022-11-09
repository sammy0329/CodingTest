moum=['a','e','i','o','u']

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    data=input()
    print(f'#{test_case} ',end='')
    for check in data:
        if check not in moum:
            print(check,end='')
    print()