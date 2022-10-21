T = int(input())
for test_case in range(1, T + 1):
    n=int(input())
    a=list(map(int, input().split()))
    sum=0
    profit=0
    while len(a) != 0:
        m=max(a)
        k=a.index(m)
        for i in range(k):
            sum+=a[i]
            profit+=m*k-sum
            a=a[k+1:]
            sum=0
    print(f"#{test_case} {profit}")