import math

def prime_factorization(n: int):
    Q = n
    t = 2
    fs = []
    print(f"{'Q':<8}{'√Q':<6}{'t':<4}{'t≤√Q':<7}{'Q≡0(mod t)':<12}{'Q=n':<6}")
    print("-" * 45)
    i = 1
    while t <= math.floor(math.sqrt(Q)):
        if Q % t == 0:
            fs.append(t)
            Q //= t
        else:
            t += 1
        
        print(i, f"{Q:<8}{math.isqrt(Q):<6}{t:<4}{str(t <= math.isqrt(Q)):<7}{str(Q % t == 0):<12}{str(Q == n):<6}")
        i += 1

    p = 0
    fs.append(Q)
    print(fs)
    for i in range(1, len(fs)):
        p += fs[i] * fs[i - 1]
        print(f"{fs[i]} × {fs[i - 1]} = {p}")

    if Q == n:
        print(n, "is prime")
    else:
        print(Q, "=", n)

prime_factorization(7)