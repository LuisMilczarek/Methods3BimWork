#!/usr/bin/env python
from typing import Callable

def oneThirdSimpson(a : float, b: float, f: Callable, n = 6) -> float:
    h = (b-a)/n
    sum_odd = 0
    sum_pair = 0
    for i in range(1, n-1):
        if i % 2 == 0:
            sum_pair += f(a+i*h)
        else:
            sum_odd += f(a+i*h)
    l = (h/3)*(f(a)+4*sum_odd+2*sum_pair+f(b))
    return l