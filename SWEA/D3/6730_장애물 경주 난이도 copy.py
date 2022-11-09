T = int(input())

for test_case in range(1, T + 1):
    N=int(input())
    data=list(map(int,input().split()))
    up=[0]
    down=[0]

    for check in range(len(data)-1):
        if data[check]>data[check+1]:
            down.append(data[check]-data[check+1])
        elif data[check]<data[check+1]:
            up.append(data[check+1]-data[check])

    print(f'#{test_case} {max(up)} {max(down)}')