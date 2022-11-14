T = 10

for test_case in range(1, T + 1):
    n=int(input())
    check=input()
    data=input()
    cnt=0
    
    for ch in range(len(data)-len(check)+1):
        if data[ch:ch+len(check)]==check:
            cnt+=1
    
    print(f'#{test_case} {cnt}')