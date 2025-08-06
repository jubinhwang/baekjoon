li2 = []

for _ in range(9):
    X = int(input())
    li2.append(X)
    
max_value = li2[0]
max_index = 0
for i in range(9):
    if max_value < li2[i]:
        max_value = li2[i]
        max_index = i
print(max_value)
print(max_index + 1)
    