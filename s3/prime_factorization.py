import math

def prime_factorization(n: int):
    Q = n
    t = 2
    fs = []
    print(f"{'Q':<8}{'√Q':<6}{'t':<4}{'t≤√Q':<7}{'Q≡0(mod t)':<12}{'Q=n':<6}")
    print("-" * 45)
    
    while t <= math.floor(math.sqrt(Q)):
        if Q % t == 0:
            fs.append(t)
            Q //= t
        else:
            t += 1
        
        print(f"{Q:<8}{math.isqrt(Q):<6}{t:<4}{str(t <= math.isqrt(Q)):<7}{str(Q % t == 0):<12}{str(Q == n):<6}")


    for t in fs:
        print(t, "x")

    if Q == n:
        print(n, "is prime")
    else:
        print(Q, "=", n)

prime_factorization(74382)