T = int(input())
for test_case in range(1, T + 1):
    n,m=map(int,input().split())
     
    li_a=list(map(int,input().split()))
    li_b=list(map(int,input().split()))
 
    max_total=-9999
 
    if n>=m:
        for j in range(n-m+1):
            total=0
            for i in range(m):
              
                total+=(li_a[i+j]*li_b[i])
     
            max_total=max(max_total,total)
    else:
        for j in range(m-n+1):
            total=0
            for i in range(n):
              
                total+=(li_a[i]*li_b[i+j])
     
            max_total=max(max_total,total)
  
    print('#{} {}'.format(test_case,max_total))
    