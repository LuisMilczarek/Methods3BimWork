#!/usr/bin/env python
from typing import Callable

def threeOctSimpson(a : float, b: float, f : Callable) -> None:
    h = (b-a)/3
    return (3*h/8)*(f(a)+3*f(a+h)+3*f(a+2*h)+f(b))