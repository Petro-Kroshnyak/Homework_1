import numpy as np
a = np.array([]).astype(int)
b = np.array([]).astype(int)
for i in range(2, 100):
    for j in range(i, 100):
        a = np.append(a, i)
        b = np.append(b, j)

sum = a+b
prod = a*b
uniq_prod = np.unique(prod)
index_del = np.array([]).astype(int)
for i in uniq_prod:
    if len(np.where(prod == i)[0]) == 1:
        for j in np.where(prod == i)[0]:
            index_del = np.append(index_del, np.where(sum == sum[j])[0])


uniq_index = np.unique(index_del)

#with np.printoptions(threshold=np.inf):
    #print(len(prod))
    #print("_____")
    #print(len(uniq_index))
    #print(uniq_index)

new_a = np.delete(a, uniq_index)
new_b = np.delete(b, uniq_index)
#print(new_a)
#print(new_b)
print(np.vstack((new_a,new_b)).T)