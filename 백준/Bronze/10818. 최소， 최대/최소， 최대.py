N = int(input())
data = list(map(int, input().split()))

li1 = []
min_value = data[0]
max_value = data[0]

for i in range(N):
    if data[i] < min_value:
        min_value = data[i]
    elif data[i] >max_value:
        max_value = data[i]

print(min_value, max_value)