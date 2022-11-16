import numpy as np
a = np.array([]).astype(int)
b = np.array([]).astype(int)
for i in range(2, 100):
    for j in range(i, 100):
        a = np.append(a, i)
        b = np.append(b, j)

summ = a+b
prod = a*b


def filter_one(e):
    if np.count_nonzero(prod == e) == 1:
        return False
    else:
        return True


def filter_two(e):
    pass_f_two = True
    for q in range(2, (e // 2) + 1):
        if not filter_one(q*(e-q)):
            pass_f_two = False
            break
    return pass_f_two


def filter_three(e):
    pass_f_three = True
    n = 0
    for q in e:
        if filter_two(f_one_a[q] + f_one_b[q]):
            n += 1
    if n != 1:
        pass_f_three = False
    return pass_f_three


def filter_four(e):
    pass_f_four = True
    n = 0
    for q in e:
        if filter_three(np.where(f_one_prod == f_two_a[q]*f_two_b[q])[0]):
            n += 1
    if n != 1:
        pass_f_four = False
    return pass_f_four


f_one_prod = np.array([]).astype(int)
f_one_a = np.array([]).astype(int)
f_one_b = np.array([]).astype(int)

for i in range(len(prod)):
    if filter_one(prod[i]):
        f_one_prod = np.append(f_one_prod, prod[i])
        f_one_a = np.append(f_one_a, a[i])
        f_one_b = np.append(f_one_b, b[i])

f_two_summ = np.array([]).astype(int)
f_two_a = np.array([]).astype(int)
f_two_b = np.array([]).astype(int)

for j in range(len(summ)):
    if filter_two(summ[j]):
        f_two_summ = np.append(f_two_summ, summ[j])
        f_two_a = np.append(f_two_a, a[j])
        f_two_b = np.append(f_two_b, b[j])

f_three_prod = np.array([]).astype(int)
f_three_a = np.array([]).astype(int)
f_three_b = np.array([]).astype(int)

for i in np.unique(f_one_prod):
    if filter_three(np.where(f_one_prod == i)[0]):
        for j in np.where(f_one_prod == i)[0]:
            f_three_prod = np.append(f_three_prod, f_one_prod[j])
            f_three_a = np.append(f_three_a, f_one_a[j])
            f_three_b = np.append(f_three_b, f_one_b[j])

f_four_summ = np.array([]).astype(int)
f_four_a = np.array([]).astype(int)
f_four_b = np.array([]).astype(int)

for i in np.unique(f_two_summ):
    if filter_four(np.where(f_two_summ == i)[0]):
        for j in np.where(f_two_summ == i)[0]:
            f_four_summ = np.append(f_four_summ, f_two_summ[j])
            f_four_a = np.append(f_four_a, f_two_a[j])
            f_four_b = np.append(f_four_b, f_two_b[j])

for i in range(len(f_three_a)):
    for j in range(len(f_four_a)):
        if f_three_a[i] == f_four_a[j] and f_three_b[i] == f_four_b[j]:
            print(f_three_a[i], f_three_b[i])
