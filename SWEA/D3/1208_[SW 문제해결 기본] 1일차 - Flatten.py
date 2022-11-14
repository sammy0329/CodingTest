from heapq import heappush,heappop

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    max_heap=[]
    min_heap=[]

    n= int(input())

    for num in list(map(int,input().split())):
        heappush(max_heap, (-num, num))
        heappush(min_heap,num)

    for i in range(n):
        max_=heappop(max_heap)
        max_=max_[1]-1
        heappush(max_heap,(-max_,max_))
        
        min_=heappop(min_heap)
        min_+=1
        heappush(min_heap,min_)

    result=heappop(max_heap)[1]-heappop(min_heap)
    print(f"#{test_case} {result}")
    
    
    
# # 단순 max,min 활용한 다른 풀이
# for i in range(1,11):
#     dump = int(input())
#     box = list(map(int, input().split()))
    
#     while dump:
#         max_box = max(box)
#         min_box = min(box)
        
#         max_idx = box.index(max(box))
#         min_idx = box.index(min(box))
        
#         box[max_idx] -= 1
#         box[min_idx] += 1
        
#         dump -= 1
        
#     print('#{} {}'.format(i,max(box)-min(box)))