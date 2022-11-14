T =10
for test_case in range(1, T + 1):
    n,string=map(str,input().split())
    n=int(n)
    string=list(string)
    check=True

 
    while check:
        for j in range(1,len(string)):
            if string[j] == string[j-1]:
                del string[j]
                del string[j-1]
                break
            
            if j==len(string)-1:
                check = False
                break
                
    print(f'#{test_case} ',*string,sep='')