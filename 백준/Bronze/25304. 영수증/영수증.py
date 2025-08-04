total_price = int(input())
item_num = int(input())
each_price = 0
for i in range(item_num):
    a, b = map(int,input().split())
    each_price += a*b
print("Yes" if total_price == each_price else "No" )