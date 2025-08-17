import math

def combinations_whitout_repeat(n: int, x: int) -> int:
    nf = math.factorial(n)
    xf = math.factorial(x)
    return int(nf / (xf * math.factorial(n - x)))

def cake_cutting_conundrum(points: int) -> int:
    """
    Se toma todas las combinaciones de los puntos para formar las lineas
    Si se toman cuatro puntos para las combinaciones es decir para formar lineas cruzadas
    Generan una insteseccion siendo haci el numero total de trozos la suma de estos.
    1 es el poligo que se forma en el centro
    """
    if points == 1:
        return 1
    
    count_lines = combinations_whitout_repeat(points, 2)
    count_interceptions = combinations_whitout_repeat(points, 4) if points > 3 else 0
    return count_lines + count_interceptions + 1

for i in range(1, 8):
    print(i, cake_cutting_conundrum(i))