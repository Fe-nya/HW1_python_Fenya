a = int(input())
b = int(input())

if a != 0:
    print(b//a)  # линейное уравнение можем решить только так

elif a == 0 and b != 0:
    print('NO')

elif a == 0 and b == 0:
    print('INF')