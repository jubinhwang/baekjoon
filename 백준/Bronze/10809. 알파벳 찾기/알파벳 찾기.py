word3 = str(input())
for i in range(97,123):
    if chr(i) in word3:
        print(word3.index(chr(i)), end = ' ')
    else:
        print("-1", end= ' ')