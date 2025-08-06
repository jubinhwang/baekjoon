N, M = map(int, input().split())
list_basket = []

for num in range(1, N+1):
    list_basket.append(num)
for _ in range(M):
    i, j = map(int, input().split())

    left = i -1
    right = j-1

    while left <right:
        list_basket[left] , list_basket[right] = list_basket[right], list_basket[left]
        left += 1
        right -= 1
        
print(*list_basket)