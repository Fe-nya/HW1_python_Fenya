x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())  # чтобы решить задачу, нам надо чтобы х и у были одного знака. Ниже:

if (x1 >= 0 and x2 >= 0 or x1 < 0 and x2 < 0) and (y1 >= 0 and y2 >= 0 or y1 < 0 and y2 < 0):
    print('YES')
else:
    print('NO')
