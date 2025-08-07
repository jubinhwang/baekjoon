T = int(input())


for i in range(T):
    j = 0
    test_list = []
    R, S = input().split()
    R = int(R)
    while True:
        if j == len(S):
            break
        else:
            
            test_list.append(S[j]*R)
            j += 1
    print(''.join(test_list))