H,M = map(int,input().split())
Min_time = int(input())
if M+Min_time >= 60:
    if(H+((M+Min_time)//60)) >=24:
        print((H+((M+Min_time)//60))-24,(M+Min_time)%60)
    else:
        print((H+((M+Min_time)//60)),(M+Min_time)%60)
else:
    print(H,M+Min_time)
   