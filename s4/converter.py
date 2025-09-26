from enum import Enum
from fractions import Fraction

class Base(Enum):
    BIN = 2
    OCT = 8
    DEC = 10
    HEX = 16

class NumberConverter:
    HEX_OFFSET = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }

    HEX_OFFSET_REVERSED = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }

    def __init__(self, expresion: str, base: Base = None):
        if base is None:
            self.data, self.base = self.__split_number_expresion(expresion)
        else:
            self.data, self.base = expresion, base
        self.has_fraction = "." in self.data

    def __split_number_expresion(self, expresion: str) -> tuple[str, Base]:
        expresion = expresion.strip().replace(" ", "")
        i = expresion.index("{")
        data = expresion[:i]
        base_int = int(expresion[i+1:-1])
        return data, Base(base_int)

    def __decimal_fraction_to(self, frac_part: str, target_base: Base, max_frac_digits: int = 20):
        rem = Fraction(int(frac_part), 10**len(frac_part))
        frac_digits = []
        pos = 0
        while rem != 0 and pos < max_frac_digits:
            rem *= target_base.value
            dig = int(rem)
            frac_digits.append(self.HEX_OFFSET.get(dig, str(dig)))
            rem -= dig
            pos += 1
        return ''.join(frac_digits)

    def __get_int_and_frac(self):
        return self.data.split(".") if self.has_fraction else (self.data, '')

    def __decimal_to(self, target_base: Base):

        int_part, frac_part = self.__get_int_and_frac()

        stack = []
        n = int(int_part)
        if n == 0:
            return NumberConverter("0", target_base)

        while n:
            k = n // target_base.value
            i = n % target_base.value
            i_str = self.HEX_OFFSET.get(i, str(i))
            print(f"{n} = {target_base.value}({k}) + {i_str}")
            stack.insert(0, i_str)
            n = k

        int_digits = "".join(stack) if stack else "0"

        if self.has_fraction:
            frac_digits = self.__decimal_fraction_to(frac_part, target_base)
            return NumberConverter(f"{int_digits}.{frac_digits}", target_base)


        return NumberConverter(int_digits, target_base)

    def __machine_to_decimal(self):
        int_part, frac_part = self.__get_int_and_frac()
        
        # int
        n = 0
        for idx, digit in enumerate((list(int_part)[::-1])):
            val = int(digit) if digit.isdigit() else self.HEX_OFFSET_REVERSED[digit.upper()]
            k = val * (self.base.value ** idx)
            print(f"{digit}*{self.base.value}^{idx} = {k}")
            n += k
        
        # frac
        if self.has_fraction:
            print("fraccion")
            frac_value = 0
            for idx, digit in enumerate(frac_part, start=1):
                val = int(digit) if digit.isdigit() else self.HEX_OFFSET_REVERSED[digit.upper()]
                k = val * (self.base.value ** -idx)
                print(f"{digit}*{self.base.value}^-{idx} = {k}")
                frac_value += k

        total = n + frac_value
        return NumberConverter(str(total), Base.DEC)

    def parse(self, target_base: Base):
        if target_base == self.base:
            print("Same base")
            return self

        match self.base:
            case Base.DEC:
                return self.__decimal_to(target_base)
            case Base.BIN | Base.OCT | Base.HEX:
                decimal = self.__machine_to_decimal()
                if target_base == Base.DEC:
                    return decimal
                return decimal.parse(target_base)

        raise NotImplementedError(f"Conversion from {self.base} not implemented")

    def __str__(self):
        return f"{self.data}{{{self.base.value}}}"


# BINARIO
c1 = NumberConverter("11.11{2}")
print("Binario a decimal:")
print(c1.parse(Base.DEC))  # 101011{2} → 43{10}

print("Binario a octal:")
print(c1.parse(Base.OCT))  # 101011{2} → 53{8}

print("Binario a hexadecimal:")
print(c1.parse(Base.HEX))  # 101011{2} → 2B{16}

