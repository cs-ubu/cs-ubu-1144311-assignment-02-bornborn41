#!/usr/pyenv/python3
from mat import *

A = readm('A.csv')
b = readm('b.csv')


def solve(A, b):
    """solve(A,b )
    A - matrix m,k
    b - matrix k,l
    x - list of solution [x_1,x_2,...,x_n]
    """

   # YOUR CODE HERE
    import numpy as np

    A, b = np.array(A), np.array(b)
    # 1. ELIMINATION
    n = len(A[0])
    x = np.array(A[0]*n)
    # print(f'n={n}')
    for k in range(n-1):
        # print(f'เลือกสมาการที่ {k}')
        for j in range(k+1, n):
            # print(f'\tกำจัดตัวแปลที่ {k},ออกจากสมการที่ {j}')
            lam = A[j][k]/A[k][k]
            A[j, k:n] = A[j, k:n] - lam*A[k, k:n]
            # print(f'\t\tlamda={lam}')
            # update b[j]
            b[j] = b[j] - lam*b[k]
        # printM(A)
        # printM(b)

    # 2. BACK SUBSTITUTION

    for k in range(n-1, -1, -1):
        # print(f'BACK SUB K= {k}')
        x[k] = (b[k] - np.dot(A[k, k+1:n], x[k+1:n]))/A[k, k]

    return x.flatten()


# print("====++ A ++====")
# printM(A)
# print("====++ b ++====")
# printM(b)
print(solve(A, b))
