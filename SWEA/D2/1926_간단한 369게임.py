N=input()
 
for i in range(1,int(N)+1):
    cnt=0
    cnt=str(i).count('3')+str(i).count('6')+str(i).count('9')
    if cnt:
        for _ in range(cnt):
            print('-',end='')
    else:
        print(i,end='')
    print(end=' ')