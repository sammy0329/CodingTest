num={'0000000': '-1','0001101': '0','0011001': '1', '0010011':'2','0111101':'3','0100011':'4','0110001':'5','0101111':'6','0111011':'7','0110111':'8','0001011':'9'}
T=int(input())

for tc in range(1,T+1):
    N,M=map(int,input().split())
    
    for i in range(N):
        row=input()
        check=[]
        odd=0
        even=0
        sum=0
        ok=True

        for j in range(0,len(row),7):
            data=num[row[j:j+7]]
            if data!='-1':
                check.append(data)

        for k in range(1,len(check)+1):
            if k%2==0:
                even+=int(check[k-1])
            else:
                odd+=int(check[k-1])
        if (odd*3+even)%10!=0:
            ok=False
            break
        else:
            sum+=odd+even

    if ok:
        print(f'#{tc} {sum}')
    else:
        print(f'#{tc} 0')
