T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    test=[]
    data=[]
    result=1
 
    for i in range(9):
        li=list(map(int,input().split()))
        data.append(li)
        if set(li) != set([1, 2, 3, 4, 5, 6, 7, 8, 9]):
            result=0
 
    for i in range(9):
        test=[]
        for j in range(9):
            test.append(data[j][i])
        if set(test) != set([1, 2, 3, 4, 5, 6, 7, 8, 9]):
            result=0
    for i in range(0,9,3):
        for j in range(0,9,3):
            test=[]
            test.append(data[i][j])
            test.append(data[i][j+1])
            test.append(data[i][j+2])
            test.append(data[i+1][j])
            test.append(data[i+1][j+1])
            test.append(data[i+1][j+2])
            test.append(data[i+2][j])
            test.append(data[i+2][j+1])
            test.append(data[i+2][j+2])
 
            if set(test) != set([1, 2, 3, 4, 5, 6, 7, 8, 9]):
                result=0
 
 
 
    print(f'#{test_case} {result}')