T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
grades=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for test_case in range(1, T + 1):
    students,target=map(int,input().split())
     
    data=[]
     
    for i in range(1,students+1):
        scores=list(map(int,input().split()))
        score=scores[0]*0.35+scores[1]*0.45+scores[2]*0.2
        data.append(score)
         
    target_data=data[target-1]
    data.sort(reverse=True)
    div = students//10
    final_k_score = data.index(target_data) // div
    print('#{} {}'.format(test_case,grades[final_k_score]))
