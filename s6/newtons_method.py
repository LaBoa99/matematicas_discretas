from typing import Callable, TypeVar, Optional

T = TypeVar("T")

def input_value(
    txt: str = "Dame un valor: ",
    fn: Optional[Callable[[str], T]] = None
) -> T | str:
    try:
        return fn(input(txt)) if fn is not None else input(txt)
    except Exception:
        print("El valor no es válido")
        raise

def input_error_precision(decimals_count: int = 12):
    return round(input_value("Dame el 'error' un numero de 0 a 1 (flotante): ", float) % 1, decimals_count)



def newton_sqrt(s: int, tol: float = 1e-2, x0=None):
    if s < 0:
        print("S es negativo")
        return
    
    if s == 0:
        return 0.0
    
    if x0 is None:
        x = s / 2.0 if s >= 1 else 1.0
    else:
        x = x0 if x0 != 0 else 1.0

    swap = s
    while swap > tol:
        x_next = (x + s / x) / 2.0
        swap = abs(x_next - x)
        x = x_next
    
    return x

a = input_value(fn=int)
e = input_error_precision()
print(newton_sqrt(a, e))
