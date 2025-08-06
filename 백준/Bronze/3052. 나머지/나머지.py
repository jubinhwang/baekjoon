list_div = []
list_remainder = [0] * 10
list_result = []
for i in range(10):
    x = int(input())
    list_div.append(x)
for j in range(10):
    list_remainder[j] = list_div[j]%42
list_result = set(list_remainder)
print(len(list_result))