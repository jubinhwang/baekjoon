N = int(input())
numbers_1 = list(map(int, input()))
number_sum = 0
for i in range(N):
    number_sum += numbers_1[i]
print(number_sum)