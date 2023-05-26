# В первом ящике находится 10 мячей, из которых 7 - белые. 
# Во втором ящике - 11 мячей, из которых 9 белых. 
# Из каждого ящика вытаскивают случайным образом по два мяча. 
# Какова вероятность того, что все мячи белые? 
# Какова вероятность того, что ровно два мяча белые? 
# Какова вероятность того, что хотя бы один мяч белый?

from math import factorial
def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

p1 = combinations(7, 2) / combinations(10, 2)
p2 = combinations(9, 2) / combinations(11, 2)
p3 = (combinations(7, 1) * combinations(3, 1) / combinations(10, 2)) * (combinations(9, 1) * combinations(2, 1) / combinations(11, 2))
p4=combinations(3, 2)/combinations(10, 2)
p5=combinations(2, 2)/combinations(11, 2)
p6 = p4 * p2
p7 = p1 * p5
result1 = p1 * p2
result2 = p7 + p3 + p6
result3 = 1 - (p4 * p5)
print(f"Вероятность того, что все мячи белые: {result1}")
print(f"Вероятность того, что ровно два мяча белые: {result2}")
print(f"Вероятность того, что хотя бы один мяч белый: {result3}")
