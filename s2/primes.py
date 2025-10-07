import math

def is_prime_one(n: int) -> bool:
    print("t", "\tt|n", "\tt = n - 1 | n=", n - 1)
    for i in range(2, n):
        print(i, "\t", n % i == 0, "\t", False)
        if n % i == 0:
            print(i, "Is a proper divisor of", n)
            return
    print(n, True, True)
    print(n, "is prime")


def is_prime_two(n: int) -> bool:
    print("t", "\tt|n", "\tt = n - 1 | n=", n // 2)
    for i in range(2, n // 2):
        print(i, "\t", n % i == 0, "\t", False)
        if n % i == 0:
            print(i, "Is a proper divisor of", n)
            return
    print(n, True, True)
    print(n, "is prime")

def is_prime_three(n: int) -> bool:
    print("t", "\tt|n", "\tt = n - 1 | n=", math.floor(math.sqrt(n)))
    for i in range(2, math.floor(math.sqrt(n))):
        print(i, "\t", n % i == 0, "\t", False)
        if n % i == 0:
            print(i, "Is a proper divisor of", n)
            return
    print(n, True, True)
    print(n, "is prime")

#is_prime_one(12497)+
is_prime_two(12497)
#is_prime_three(12497)