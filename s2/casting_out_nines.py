def casting_out_nines(n: int) -> int:
    k = n
    while k > 9:
        digits = [int(x) for x in list(str(k))]
        digits_sum = sum(digits)
        print(digits, "=", digits_sum)
        k = digits_sum
    return k == 3 or k == 6 or k == 9

print(casting_out_nines(87466))