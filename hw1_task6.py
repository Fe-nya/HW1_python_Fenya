import math
a = int(input())
b = int(input())
c = int(input())
if a != 1:
    b = b//a
    c = c//a
    a = 1
x1 = (((-b) + (math.sqrt((b ** 2 - 4 * a * c)))) / (2 * a))
x2 = (((-b) - (math.sqrt((b ** 2 - 4 * a * c)))) / (2 * a))
if x1 != 0 and x2 != 0:
    print(x1, x2)
elif x1 == 0 and x2 != 0:
    print(x2)
elif x1 != 0 and x2 == 0:
    print(x1)
elif x1 == 0 and x2 == 0:
    print()
