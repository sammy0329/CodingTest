T=10
for test_case in range(1,T+1):
    n=int(input())
    dataset=list(map(int,input().split()))
    
    cmd=int(input())
    comand=list(map(str,input().split()))
    
    for i in range(len(comand)):
        if comand[i]=='I':
            for j in range(int(comand[i+2])):
                
                dataset.insert(int(comand[i+1])+j,comand[i+3+j])
    
    print('#{} {} {} {} {} {} {} {} {} {} {}'.format(test_case,*dataset[:10]))