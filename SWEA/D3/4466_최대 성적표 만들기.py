
T=int(input())
for tc in range(1,T+1):
    N,K=map(int,input().split())
    dataset=list(map(int,input().split()))
    total=0
    for i in range(K):
        total+=dataset.pop(dataset.index(max(dataset)))
    print(f'#{tc} {total}')