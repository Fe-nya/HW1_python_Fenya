price = input().split()  # считываем результат, полученный от программы

one = int(price[0])
two = int(price[1])
three = int(price[2])

c1 = one * 15
c2 = two * 125
c3 = three * 440  # считаем стоимость

print(c1, c2, c3)
print('Itogo: ', c1 + c2 + c3)  # видим стоимость и сравниваем с желаемой
