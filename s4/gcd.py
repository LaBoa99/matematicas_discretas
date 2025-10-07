def gcd(x: int, y: int) -> int:
    a = x
    b = y
    r = a % b

    print(f"{'a':>10} {'b':>10} {'r':>10} {'r > 0':>10}")
    print(f"{a:>10} {b:>10} {r:>10} {str(r > 0):>10}")

    while r > 0:
        a = b
        b = r
        r = a % b
        print(f"{a:>10} {b:>10} {r:>10} {str(r > 0):>10}")
    
    print(f"\nGCD({x}, {y}) = {b}")
    return b



gcd(10035, 3568)