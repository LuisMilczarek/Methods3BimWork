#/usr/bin/env python
from typing import List
def lagrange(xi : List[float], yi: List[float],x) -> float:
    '''
    Get's the lagrande interpolation value.
    Parametesrs:
    xi: x values of the data
    yi: y values of the data
    x: target x for the interpolation
    Returns:
    y float value

    '''
    n = len(xi)-1
    sum = 0
    for i in range(n+1):
        l =1
        for j in range(n+1):
            if i!=j:
                l *= (x - xi[j])/(xi[i] - xi[j])
        sum += l *yi[i]
    return sum
