#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from interpolators import lagrange
from regression import minSquares
from integration import trapeze, oneThirdSimpson, threeOctSimpson
from utils import report
import os

def do_report(data: dict) -> None:
    print("\nRelatório:")
    for k, v in data.items():
        print(f"\t{k}: {v}")
    print("")


def Pt(t: float) -> float:
    y = 0.2*np.power(t,3) -1.5*np.power(t,2)+4*np.sin(t)+2*np.cos(t) +10
    return y

def Et(t : float) -> float:
    y = (0.2*np.power(t,4))/4 -(1.5*np.power(t,3))/3 - 4*np.cos(t) + 2*np.sin(t) +10*t
    return y

def main1() -> None:
    print("\n\nParte 1:\n\n")
    base_path = "./graficos"
    z = 25
    xi = [ 0,     10,   20,   30,   40,   50]
    yi = [20.0, 23.5, 30.0, 33.2, 40.1, 45.2]
    
    print("#"*10,"LAGRANCE","#"*10)

    n_yi = [lagrange(xi,yi,y) for y in yi]
    y = lagrange(xi,yi,z)
    plt.title("Lagrange")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Temperatura (ºC)")
    plt.plot(xi,yi,label="Valores reais", marker="o", markersize=5)
    plt.plot(xi, n_yi, marker="o", markersize=5)
    plt.plot(z, y, marker="o", markersize=5)
    plt.savefig(f"{base_path}/lagrange.png")


    print(y)
    do_report(report(yi, n_yi))

    print("#"*10,"MINIMOS QUADRAROS","#"*10)
    coefs = minSquares(xi,yi)
    print(f"Coef: {coefs}")
    print(coefs[1]*z+ coefs[0])

    n_yi = [coefs[0]+coefs[1]*x for x in xi]
    for x, y in zip(xi, n_yi):
        print(f"x:{x}, y: {y}; ",end="")
    print("")

    plt.title("Minimos Quadrados")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Temperatura (ºC)")

    plt.plot(xi,yi, label="Valores reais", marker="o", markersize=5)
    plt.plot(xi,n_yi, label="Valores estimados", marker="o", markersize=5)
    plt.plot(z,coefs[0]+coefs[1]*z, label="Instante desejado",marker="o", markersize=5)

    plt.legend()
    plt.savefig(f"{base_path}/min_quadrados.png")

    do_report(report(yi, n_yi))
    # plt.show()

def main2() -> None:
    A = 0
    B = 6
    BASE_PATH = "./graficos"

    ans = 16.400488
    print("\n\nParte 2:\n\n")

    print("#"*10,"Trapezio","#"*10)
    E_total = trapeze(0,6,Pt)
    print(f"Energia total: {E_total} w/s")
    err = ans - E_total
    err_per = abs(err)/ans
    print(f"Erro absoluto: {err}, erro percentual: {err_per}\n")

    print("#"*10,"1/3 de simpson:","#"*10)
    E_total = oneThirdSimpson(A,B,Pt)
    print(f"Energia total: {E_total} w/s")
    err = ans - E_total
    err_per = abs(err)/ans
    print(f"Erro absoluto: {err}, erro percentual: {err_per}\n")

    print("#"*10,"3/8 de simpson:","#"*10)
    E_total = threeOctSimpson(A,B,Pt)
    print(f"Energia total: {E_total} w/s")
    err = ans - E_total
    err_per = abs(err)/ans
    print(f"Erro absoluto: {err}, erro percentual: {err_per}\n")

    #Grafico de erros


    # it
    err_trapezio = []
    err_one_third = []

    err_perc_trapezio = []
    err_perc_one_third = []
    seg =[]

    for i in range(6,1000):
        seg.append(i)

        value = trapeze(0,6,Pt,i)
        err = ans - value
        err_per = abs(err)/ans
        err_trapezio.append(err)
        err_perc_trapezio.append(err_per)

        value = oneThirdSimpson(0,6,Pt,i)
        err = ans - value
        err_per = abs(err)/ans
        err_one_third.append(err)
        err_perc_one_third.append(err_per)
    
    plt.title("Erro absoluto")
    plt.plot(seg, err_trapezio, label="Trapezio")
    plt.plot(seg, err_one_third, label="1/3 de Simpson")
    plt.xlabel("Segmentos")
    plt.ylabel("Erro (ºC)")
    plt.legend()

    plt.savefig(f"{BASE_PATH}/err_absoluto.png",dpi=300)

    plt.clf()

    plt.title("Erro percentual")
    plt.plot(seg, err_perc_trapezio, label="Trapezio")
    plt.plot(seg, err_perc_one_third, label="1/3 de Simpson")
    plt.xlabel("Segmentos")
    plt.ylabel("Erro (%)")
    plt.legend()

    plt.savefig(f"{BASE_PATH}/err_perc.png",dpi=300)



if __name__ == "__main__":
    if not os.path.exists("./graficos/"):
        os.mkdir("./graficos/")
    main1()
    main2()