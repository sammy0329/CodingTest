T=int(input())
 
for i in range(1,T+1):
    n=int(input())
    data=list(map(int,input().split()))
    profit=0
    max_data=data[-1]
    for j in range(n-1,-1,-1):
        if data[j]>max_data:
            max_data=data[j]
        else:
            profit=profit+(max_data-data[j])
    print('#{} {}'.format(i,profit))