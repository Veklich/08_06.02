# Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. Стрелок выстрелил 100 раз. 
# Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.

from math import factorial
def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))
n = 100
p = 0.8
k = 85
q = 1 - p
result = combinations(n, k) * (p ** k) * (q ** (n-k)) 
print(f'Вероятность того, что стрелок попадет в цель ровно 85 раз: {result}')