T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a=input()
    check=True
    for i in range(len(a)//2):
        if a[i]!=a[len(a)-i-1]:
            check=False
            break
        else:
            check=True
    if check:
        print('#{} {}'.format(test_case,1))
    else:
        print('#{} {}'.format(test_case,0))