import numpy as np
from typing import List

def report(y1 : List[float], y2 : List[float]) -> dict:
    y1 = np.array(y1)
    y2 = np.array(y2)
    erros = y1 - y2
    vari = np.var(erros)
    desvio = np.sqrt(vari)
    return {"variancia": vari, "desvio":desvio}