#!/usr/bin/env python
import numpy as np
from typing import List

def minSquares(xi : List[float], yi : List[float]) -> List[float]:
    n = len(xi)
    sum_x = sum(xi)
    sum_y = sum(yi)
    sum_xy = sum([x*y for x,y in zip(xi,yi)])
    sum_x2 = sum([x*x for x in xi])

    mean_x = sum_x/n
    mean_y = sum_y/n

    a1 = (n*sum_xy -sum_x*sum_y)/(n*sum_x2-sum_x*sum_x)
    a0 = (sum_y - a1*sum_x)/n

    st = 0
    sr = 0

    for i in range(n):
        st += np.power(yi[i]-mean_y,2)
        sr += np.power(yi[i]-a1*xi[i]-a0,2)

    syx = np.sqrt((sr/(n-2)))
    r2 = (st -sr)/st
    print(f"syx: {syx}, r2: {r2}")
    return [a0,a1]