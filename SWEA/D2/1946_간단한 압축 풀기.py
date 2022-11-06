T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    li=[]
    count=0
    for _ in range(n):
        ch=tuple(map(str,input().split()))
        li.append(ch)
    print(f'#{test_case}')
    for i in li:
        for j in range(int(i[1])):
            count+=1
            if count>10:
                print()
                count=1
 
            print(i[0],end='') 
    print()