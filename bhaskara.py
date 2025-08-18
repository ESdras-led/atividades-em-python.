#fazer uma "calculadora" para calcular bhaskara

import math


print("calculadora de formula de bhaskara:")

def calcular_bhaskara():

    a = int(input("digite o valor de A:"))
    b = int(input("digite o valor de B:"))
    c = int(input("digite o valor de C:"))

    print(f"{b}²-4.a.c")

    Δ = b ** 2 -4*a*c
    if Δ < 0:
            print("o delta é menor que zero então o resultado é {Δ} e fica inconclusivo para o resto da formula")
        
            

    print(f"o valor de delta é:{Δ}")

    print("agora usando o delta iremos descobrir as duas raizes x1 e x2")

    xa = -b + math.sqrt(Δ)
    x1 = xa/2*a

    
    xb = -b - math.sqrt(Δ)
    x2 = xb/2*a
    
    print(f"raiz x1 de delta é:{x1}")
    print(f"raiz x2 de delta é:{x2}")


calcular_bhaskara()
