x, y = int(input()), int(input())
if x % 2 == 0 and y % 2 == 0:
    total = x + y
    print(total)
elif x % 2 != 0 and y % 2 != 0:
    product = x * y
    print(product)
elif x % 2 == 0 and y % 2 != 0 or x % 2 != 0 and y % 2 == 0:
    diff = max(x, y) - min(x, y)
    print(diff)
