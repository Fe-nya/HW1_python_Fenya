x = int(input())

ten = x // 10
one = x % 10

if ten == 10:  # преобразуем десятки
    result = 'C'
elif ten == 9:
    result = 'XC'
elif ten == 4:
    result = 'XL'
elif ten >= 5:
    result = 'L' + (ten - 5) * 'X'
else:
    result = ten * 'X'


if one == 9:  # разберемся с единицами
    result += 'IX'
elif one == 4:
    result += 'IV'
elif one >= 5:
    result += 'V' + (one - 5) * 'I'
else:
    result += one * 'I'


print(result)

