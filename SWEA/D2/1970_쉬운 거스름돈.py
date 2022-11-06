T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    money=[50000,10000,5000,1000,500,100,50,10]
    print('#{} '.format(test_case))
    for i in money:
        print(n//i,end=' ')
        n%=i
    print()