chess = [1,1,2,2,2,8]
DH = list(map(int, input().split()))

result = [chess[i]-DH[i] for i in range(len(chess))]
print(*result)