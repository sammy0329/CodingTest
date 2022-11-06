T = int(input())
for test_case in range(1, T + 1):
    n=int(input())
    arr=[]
    output=[[] for _ in range(n)]
    for i in range(n):
        arr.append(list(map(int,input().split())))
 
    for j in range(n):
        string=''
        for k in range(n-1,-1,-1):
 
            string+=str(arr[k][j])
        output[j].append(string)
 
    for l in range(n-1,-1,-1):
        string=''
        for m in range(n-1,-1,-1):
            string+=str(arr[l][m])
 
        output[n-l-1].append(string)
 
    for l in range(n-1,-1,-1):
        string=''
        for m in range(n):
            string+=str(arr[m][l])
 
        output[n-l-1].append(string)
    print(f'#{test_case}')       
    for i in range(n):
        for j in range(3):
            print(output[i][j], end=' ')
        print()