T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
 
    n,m=map(int,input().split())
    data=[[] for _ in range(n)]
    max=-1
     
    for i in range(n):
        data[i]=list(map(int,input().split()))
      
    for j in range(n-m+1):
        for k in range(n-m+1):
            sum=0
            for l in range(m):
                for o in range(m):
                    sum+=data[j+l][k+o]
 
            if sum>max:
                max=sum
    print('#{} {}'.format(test_case,max))