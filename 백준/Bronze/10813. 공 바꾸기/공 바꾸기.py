N, M = map(int, input().split())

arr = []
x = 0
for q in range(1, N+1):
    arr.append(q)
for _ in range(M):
    i,j = map(int, input().split())
    x = arr[i-1]   
    arr[i-1] = arr[j-1] 
    arr[j-1] = x 
print(*arr)