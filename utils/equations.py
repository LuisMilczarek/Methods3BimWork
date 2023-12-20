from typing import List
import numpy as np
def applyEquation(x : float, fx : List[float]) -> float:
    y = 0
    for i, c in enumerate(fx):
        y += np.power(x,i)*c

    return y