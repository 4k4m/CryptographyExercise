import numpy as np
v1 = np.array([846835985, 9834798552])
v2 = np.array([87502093, 123094980])
m = -1
while(m != 0):
    if (np.dot(v2, v2) < np.dot(v1, v1)):
        t = v1
        v1 = v2
        v2 = t
    m = int((v1.dot(v2)) / (v1.dot(v1)))
    if(m == 0):
        print(v1.dot(v2))
    v2 = v2 - m*v1