# Demostración del Algoritmo de Bisección

import math

# Función para definir la función matemática a evaluar.
def definir_funcion(fun):
    def f(x):
        return eval(fun, {"x": x})
    return f    

# Función para determinar el valor de A y B.
def determinar_a_b(fun, t: int):
    # f(a) < T < f(b)
    a = 0  # Valor inicial de A
    b = 1  # Valor inicial de B
    f = definir_funcion(fun)
    while True:
        f_a = f(a)
        f_b = f(b)
        if f_a < t < f_b:
            return a, b
        a += 1
        b += 1  
    return a, b 

# Función principal que implementa el algoritmo de bisección.
def biseccion_metodo(fun, t: int, delta: float):
    f = definir_funcion(fun)
    a,b = determinar_a_b(fun, t)

    # Se realiza el algortmo de bisección.

    # Se determina el punto intermedio (z).
    z = (a + b) / 2

    while abs(z - a) >= delta:
        if f(z) <= t:
            a = z
        if f(z) >= t:
            b = z
        z = (a + b) / 2
        # Imprime los resultados de cada iteración.
        print(f"{a:<20}{z:<20}{b:<20}{abs(z-a):<20}{f(z):<20}")
    # Imprime los resultados finales.
    print(f"{a:<20}{z:<20}{b:<20}{abs(z-a):<20}{f(z):<20}")


# Se imprime los encabezados de la tabla.
def imprimir_tabla():
    print(f"{'A':<20}{'z':<20}{'B':<20}{'|z - A|':<20}{'f(z)':<20}")
    print("--------------------------------------------------------------------------------------------------------")

# Se pide al usuario los valores de la función, T y delta, y se llama a la función principal.
def main():
    fun = input("f(x): ")
    t = int(input("f(x) = T, ingresa T: "))  
    delta = float(input("error permitido (ejem. 0.001): "))
    imprimir_tabla()
    biseccion_metodo(fun, t, delta)

main()