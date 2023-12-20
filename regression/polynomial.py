#!/usr/bin/env python
import numpy as np
from typing import List

def normalEquation(xi: List[float], yi: List[float], m: int) -> List[np.ndarray]:
    n = len(xi)
    a = np.zeros((m + 1, m + 1))
    b = np.zeros(m + 1)

    for i in range(m + 1):
        for j in range(i + 1):
            k = i + j - 2
            soma = 0
            for l in range(n):
                soma += np.power(xi[l], 1 + k)
            a[i][j] = soma
            a[j][i] = soma

        soma = 0
        for l in range(n):
            soma += yi[l] * np.power(xi[l], i)
        b[i] = soma

    return [b, a]

def polynomialRegression(xi: List[float], yi: List[float], m: int) -> List[float]:
    n = len(xi)
    if n < m + 1:
        raise ValueError("Not enough data points for the specified degree of the polynomial")

if __name__ == "__main__":
    xi = [0, 10, 20, 30, 40, 50]
    yi = [20.0, 23.5, 30.0, 33.2, 40.1, 45.2]

    bi, a = normalEquation(xi, yi, 4)
    print(f"bi: {bi}, a:{a}")
