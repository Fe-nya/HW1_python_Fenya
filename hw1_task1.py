k = int(input())
m = int(input())
n = int(input())
p = n // k
if n%k != 0:
    p += 1
print(p * m * 2)