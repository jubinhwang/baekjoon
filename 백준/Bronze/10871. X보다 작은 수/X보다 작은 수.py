N,X = map(int, input().split())
numbers = list(map(int, input().split()))
list1 = []
for i in range(N):
    if numbers[i] < X:
        list1.append(numbers[i])
print(*list1)
    