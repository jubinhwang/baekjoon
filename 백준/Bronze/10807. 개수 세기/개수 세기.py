N = int(input())
numbers = list(map(int, input().split()))
V = int(input())
answer = 0
for i in range(N):
    if numbers[i] == V:
        answer += 1
print(answer)