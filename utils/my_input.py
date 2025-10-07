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

print(input_error_precision())
