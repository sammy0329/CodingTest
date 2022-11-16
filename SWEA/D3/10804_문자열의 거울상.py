data={'b':'d','d':'b','q':'p','p':'q'}
T=int(input())

for test_case in range(1,T+1):
    s=input()
    str=''
    for check in range(len(s)-1,-1,-1):
        str+=data[s[check]]
    print(f'#{test_case} {str}')
