n = int(input())
one = n % 10
two = n // 10
three = n // 60  # вспомогательные переменные для каждой цены


if n <= 8:  # больше 8 выгодней второй тариф
    print(n, 0, 0)


elif 8 < n <= 30:   # больше 30 выгодней третий тариф
    if one >= 8:  # не забываем про первый тариф
        print(0, two + 1, 0)
    else:
        print(one, two, 0)


elif n > 30:
    if n <= 60:  # проверяем выгодней купить по первому или второму или сразу по третьему один
        if one <= 4:
            print(one, two, 0)
        else:
            print(0, 0, 1)


    else:  # для большого количества билетов
        i = n - three * 60
        if i >= 31:
            if one <= 4:  # также не забываем про первый тариф
                print(one, i // 10, three)
            else:
                print(0, 0, three + 1)
        else:
            if one >= 8:   # также не забываем про первый тариф
                print(0, i // 10 + 1, three)
            else:
                print(one, i // 10, three)
