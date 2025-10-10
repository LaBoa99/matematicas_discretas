def complemento_2(n: int, bits: int = 8) -> int:
    max_val = 2 ** bits
    return (~n + 1) & (max_val - 1)

print(bin(complemento_2(255)))  # Salida: 0b10100001
print(complemento_2(255))       # Salida: 161