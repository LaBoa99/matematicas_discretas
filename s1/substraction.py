# Three Substraction Algorithms

# 89 = 8, 9 => 80, 9
def expand_number(n: int) -> list[int]:
    pointer = 10
    digits = []
    index = 0

    while n > 0:
        part = n % pointer
        part *= 10 ** index
        n //= pointer
        digits.append(part)
        index += 1
    
    return digits

def borrow_substraction(a: int, b: int) -> int:
    a_expanded = expand_number(a)
    b_expanded = expand_number(b)

    # borrow
    a_size = len(a_expanded)
    
    if a_size > 1:
        a_expanded[0] += 10
        a_expanded[1] -= 10
    
    b_size = len(b_expanded)

    if a_size < b_size:
        a_expanded += [0] * (b_size - a_size)
        a_size = b_size
    elif b_size < a_size:
        b_expanded += [0] * (a_size - b_size)
        b_size = a_size

    result = 0
    for i in range(a_size):
        result += a_expanded[i] - b_expanded[i]

    return result

def carrying_substraction(a: int, b: int) -> int:
    a_expanded = expand_number(a)
    b_expanded = expand_number(b)

    # borrow
    a_size = len(a_expanded)
    
    a_expanded[0] += 10
    b_expanded[-1] += 10
    
    b_size = len(b_expanded)

    if a_size < b_size:
        a_expanded += [0] * (b_size - a_size)
        a_size = b_size
    elif b_size < a_size:
        b_expanded += [0] * (a_size - b_size)
        b_size = a_size

    result = 0
    for i in range(a_size):
        result += a_expanded[i] - b_expanded[i]
        
    return result

def complementation_substraction(a: int, b: int) -> int:
    a_size = len(str(a))
    a_nines = 10 ** a_size 
    diff = a_nines - b
    complement = a + diff
    return complement - a_nines


print(complementation_substraction(86, 38))