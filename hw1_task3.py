n = int(input())
one = n % 10
two = n // 10
three = n // 60

if n <= 8:
    print(n, 0, 0)


elif 8 < n <= 30:
    if one >= 8:
        print(0, two + 1, 0)
    else:
        print(one, two, 0)


elif n > 30:
    if n <= 60:
        if one <= 4:
            print(one, two, 0)
        else:
            print(0, 0, 1)

    else:
        i = n - three * 60
        if i >= 31:
            if one <= 4:
                print(one, i // 10, three)
            else:
                print(0, 0, three + 1)
        else:
            if one >= 8:
                print(0, i // 10 + 1, three)
            else:
                print(one, i // 10, three)
