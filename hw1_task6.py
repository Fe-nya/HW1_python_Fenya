a = int(input())
b = int(input())
c = int(input())
if a != 1:
    b = b//a
    c = c//a
    a = 1
i = (b ** 2 - 4 * a * c)
x1 = (((-b) + (i ** 0.5)) / (2 * a))
x2 = (((-b) - (i ** 0.5)) / (2 * a))

if x1 == x2:
    print(x1)
elif x1 == 0 and x2 == 0:
    print()
else:
    print(x1, x2)