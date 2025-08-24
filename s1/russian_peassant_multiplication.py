def russian_peassant_multiplication(m: int, n: int) -> int:
    result = 0
    while n > 0:
        # Solo tomamos los valores impares
        if n % 2 != 0:
            result += m
        n //= 2
        m *= 2
    return result

print(russian_peassant_multiplication(20, 3))


