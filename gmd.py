# minimo comun divisor euclides
def euclides(n, m):
    r = n % m
    print(f"{'n':<8}{'m':<8}{'r':<8}")
    print("-" * 24)
    print(f"{n:<8}{m:<8}{r:<8}")
    while r != 0:
        n = m
        m = r
        r = n % m
        print(f"{n:<8}{m:<8}{r:<8}")
    return m

print(euclides(10035, 3568))
print(1.6 * 10**-3)