from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import ThreadPool

import numpy as np
from numpy._core.multiarray import _reconstruct


def build_permutation_matrix(ipvt):
    n = len(ipvt)
    P = np.eye(n)
    for k in range(n - 1):
        i = k
        j = ipvt[k]

        if i != j:
            P[[i, j]] = P[[j, i]]

    return P


def lu_factor_parallel_with_lu(A):
    A = A.copy()
    n = A.shape[0]
    ipvt = np.arange(n)
    info = 0

    for k in range(n - 1):
        pivot_row = k + np.argmax(np.abs(A[k:, k]))
        ipvt[k] = pivot_row

        if pivot_row != k:
            A[[k, pivot_row], :] = A[[pivot_row, k], :]

        if A[k, k] == 0:
            info = k
            continue

        A[k + 1 :, k] /= A[k, k]

    def saxpy(j):
        A[k + 1 :, j] -= A[k, j] * A[k + 1 :, k]

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(saxpy, j) for j in range(k + 1, n)]
        for f in futures:
            f.result()

    if A[n - 1, n - 1] == 0:
        info = n - 1

    L = np.tril(A, k=-1) + np.eye(n, dtype=A.dtype)
    U = np.triu(A)

    return L, U, ipvt, info


A = np.array([[2, 3, 1], [4, 7, 7], [6, 18, 22]], dtype=float)

L, U, ipvt, info = lu_factor_parallel_with_lu(A)

print("Matriz original:")
print(A)

print("\nL (triangular inferior):")
print(L)

print("\nU (triangular superior):")
print(U)

print("\nPivot indices:", ipvt)
print("Info", info)

P = build_permutation_matrix(ipvt)

reconstructed = P @ A

LU = L @ U

print("\nP @ A:")

print(LU)

print("\Erro (norma Frobenius):", np.linalg.norm(reconstructed - LU))
