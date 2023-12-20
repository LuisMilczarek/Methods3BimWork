#!/usr/bin/env python
from typing import Callable

def trapeze(a : float, b : float, f : Callable, n : int = 6) -> float:
    h = (b - a)/n
    summ = f(a) + f(b)
    for i in range(1, n-1):
        xi = a + i*h
        summ += 2*f(xi)
    l = (h/2)*summ
    return l