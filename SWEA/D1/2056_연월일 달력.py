#YYYY/MM/DD
 
T = int(input())
month_31=[1,3,5,7,8,10,12]
month_30=[4,6,9,11]
month_28=[2]
 
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a=input()
    month=int(a[4:6])
    day=int(a[6:])
    if month in month_31:
        if day>31:
            a=-1
    elif month in month_30:
        if day>30:
            a=-1
    elif month in month_28:
        if day>28:
            a=-1
    else:
        a=-1
    if a==-1:
        print('#{} {}'.format(test_case,(-1)))
    else:
 
             
        print('#{} {}'.format(test_case,(a[:4]+'/'+a[4:6]+'/'+a[6:])))