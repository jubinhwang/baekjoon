N = int(input())
list_score = list(map(int, input().split()))

fix_list_score = [0]*N
total_score = 0

list_score.sort()
M = list_score[-1]

for j in range(N):
    fix_list_score[j] = (list_score[j]/M)*100
    total_score += fix_list_score[j]

score_mean = total_score/N
print(f'{score_mean: .6f}')