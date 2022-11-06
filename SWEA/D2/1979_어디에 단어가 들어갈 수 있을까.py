T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    m,k=map(int,input().split())
    li=[[] for _ in range(m)]
    li_t=[[] for _ in range(m)]
     
 
    yes=0
    for i in range(m):
        cnt=0
        data=list(map(int,input().split()))
        li[i]=data        
        for j in range(len(data)):
            li_t[j].append(data[j])
            if data[j]==1:
                cnt+=1
                if j==(m-1):
                    if cnt==k:
                        yes+=1
 
            else:
                if cnt==k:
                    yes+=1
                cnt=0
             
    for w in range(m):
        cnt=0
        for l in range(m):
            if li_t[w][l]==1:  
                cnt+=1
                if l==(m-1):
                    if cnt==k:
                        yes+=1
            else:
                if cnt==k:
                    yes+=1
                cnt=0
             
    print(f'#{test_case} {yes}')