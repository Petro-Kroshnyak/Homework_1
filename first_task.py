import numpy as np
n = 0
for i in range(10000):
    a = 2 * np.random.random_sample(2) - 1
    if a[0]**2 + a[1]**2 <= 1:
        n += 1
pi = 4*(n/10000)
print(pi)
