# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

from math import factorial
def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))
n = 144
p = 0.5
k = 70
q = 1 - p
result = combinations(n, k) * (p ** k) * (q ** (n-k)) 
print(f"Вероятность, что орел выпадет ровно 70 раз: {result}")