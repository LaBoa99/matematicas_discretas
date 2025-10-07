def biseccion(fn: str, t: float, tol: float):
    def f(function: str, x: float) -> float:
        return eval(function.replace("x", str(x)))
    
    def g(x: float) -> float:
        return f(fn, x) - t
    
    # Buscar un intervalo automáticamente
    a, b = -1.0, 1.0
    while g(a) * g(b) > 0:
        a *= 2
        b *= 2
    
    # Encabezado
    print(f"{'A':<12}{'z':<12}{'B':<12}{'|z - A|':<12}{'f(z)':<12}")
    
    z = (a + b) / 2
    while abs(g(z)) >= tol:
        print(f"{a:<12.6f}{z:<12.6f}{b:<12.6f}{abs(z - a):<12.6f}{f(fn, z):<12.6f}")
        
        if g(a) * g(z) < 0:
            b = z
        else:
            a = z
        z = (a + b) / 2
    
    print(f"{a:<12.6f}{z:<12.6f}{b:<12.6f}{abs(z - a):<12.6f}{f(fn, z):<12.6f}")
    
    return z


# === Entrada por consola ===
formula = input("Ingresa la función en términos de x (ej: x**2 + 2): ")
T = float(input("Ingresa el valor de T (ej: 10): "))
tol = float(input("Ingresa la tolerancia (ej: 0.0001): "))

resultado = biseccion(formula, T, tol)
print("\nResultado aproximado:", resultado)
