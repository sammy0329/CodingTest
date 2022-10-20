p,k=map(int,input().split())
result=0
 
if p>=k:
    result=p-k+1
else:
    result=999-k+p+1
     
print(result)