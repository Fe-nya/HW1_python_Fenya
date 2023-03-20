n = int(input())
i = n % 10  # для упрощения подсчетов

if 5 <= i or i == 0 or 11 <= n <= 19:   # просто правила русского
    print(n, 'korov')
elif i == 1:
    print(n, 'korova')
elif 2 <= i <= 4:
    print(n, 'korovy')

