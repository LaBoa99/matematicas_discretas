# Ignacio Andrade
import math


def pedir_numero():
    while True:
        try:
            num = int(input("Ingrese un número entero positivo: "))
            if num > 0:
                return num
            else:
                print("❌ Error: el número debe ser positivo.")
        except ValueError:
            print("❌ Error: debe ingresar un número entero.")


def factorizar(n):
    Q = n
    t = 2
    factores = []

    print(f"{'Q':<10}{'√Q':<8}{'t':<5}{'t <= √Q':<10}{'t|Q':<6}{'Q=n':<6}{'output-so-far'}")
    print("-" * 60)

    while t <= math.isqrt(Q):
        condicion = "T" if t <= math.isqrt(Q) else "F"
        divisible = "T" if Q % t == 0 else "F"

        if Q % t == 0:
            factores.append(t)

        print(
            f"{int(Q):<10}"
            f"{math.isqrt(Q):<8}"
            f"{t:<5}"
            f"{condicion:<10}"
            f"{divisible:<6}"
            f"{'-':<6}"
            f"{' x '.join(map(str, factores))} "
            # f"{'x' if divisible == 'T' else ''}"
        )

        if Q % t == 0:
            Q //= t
        else:
            t += 1

    if Q==n:
        finalizar = "T"
    else:
        finalizar = "F"

    # si queda un número primo mayor a 1
    if Q > 1:
        factores.append(Q)
        print(f"{int(Q):<10}"
              f"{math.isqrt(Q):<8}"
              f"{t:<5}"
              f"{'F':<10}"
              f"{'-':<6}"
              f"{finalizar:<6}"
              f"{' x '.join(map(str, factores))}"
              )

    # resultado final
    print("\nResultado final:")
    if finalizar=="T":
        print(f"El número {n} es primo")
    else:
        print(f"El número {n} se puede factorizar en:")
    print(" × ".join(map(str, factores)), "=", n)

#
n = pedir_numero()
factorizar(n)
# factorizar(74382)
# factorizar(167)