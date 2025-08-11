word1 = input()
word1 = list(word1)
word1_sum = 0
for i in range(len(word1)):
    if word1[i] in "ABC":
        word1_sum += 3
    elif word1[i] in "DEF":
        word1_sum += 4
    elif word1[i] in "GHI":
        word1_sum += 5
    elif word1[i] in "JKL":
        word1_sum += 6
    elif word1[i] in "MNO":
        word1_sum += 7
    elif word1[i] in "PQRS":
        word1_sum += 8
    elif word1[i] in "TUV":
        word1_sum += 9
    elif word1[i] in "WXYZ":
        word1_sum += 10
print(word1_sum)