T = 1

for test_case in range(1, T + 1):
    n=int(input())
    result=0
    minus=[]
    for j in range(n):
        row=list(map(int,input()))
        result+=sum(row)

        print(sum(row[:n//2-j]),sum(row[:-(n//2-j)-1:-1]))
        # result-=sum(row[:n//3-j+1])
        # result-=sum(row[-1:-(n//3-j+1)-1:-1])
        
    print(f'#{test_case} {result}')