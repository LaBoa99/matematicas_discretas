class ArimeticAccountant:
    
    def precedence(self, op: str):
        return {
            "-": 1,
            "+": 1,
            "*": 2,
            "/": 2
        }.get(op, 1)
    
    def rpn(self, tokens: list[str]) -> list[str]:
        stack = []
        output = []

        for token in tokens:
            if token.isdigit():
                output.append(token)
            else:
                while stack and self.precedence(stack[-1]) >= self.precedence(token):
                    output.append(stack.pop())
                stack.append(token)
        while stack:
            output.append(stack.pop())
        return output

    def calculate(self, tokens: list[str], steps: int = -1, offset: int = 0) -> list:
        stack = []
        current_step = 1
        print("Calculate", tokens)
        for i in range(offset, len(tokens)):
            token = tokens[i]
            if str(token).isdigit():
                stack.append(int(token))
                continue
            
            if len(stack) == 1:
                return stack

            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a // b) 
            if current_step == steps:
                return stack + tokens[3*steps::]
            
            current_step += 1
        return stack

    def init(self, str_operation: str):
        tokens: list[str] = str_operation.split(" ")
        return self.calculate(self.rpn(tokens))[0]

        
class MasterAritmeticAccountant(ArimeticAccountant):

    def cast_to_nines(self, n: int) -> int:
        k = abs(n)
        while k > 9:
            digits = [int(x) for x in list(str(k))]
            digits_sum = sum(digits)
            k = digits_sum
        return k if n >= 0 else -k

    def normalize_rpn_to_nines(self, numbers: list[str]) -> list[str]:
        length = len(numbers)
        all_single_digit = False
        while not all_single_digit:
            all_single_digit = True
            for i in range(length):
                if str(numbers[i]).isdigit() and len(str(numbers[i])) > 1:
                    numbers[i] = str(self.cast_to_nines(int(numbers[i])))
                    all_single_digit = False
            print("NINES: ", numbers)
        return numbers

    def init(self, str_operation):
        if "/" in str_operation:
            print("[WARNING] LA DIVISION NO PERMITE LA VALIDACION EN NUEVES CORRECTA")

        tokens: list[str] = str_operation.split(" ")
        numbers = self.rpn(tokens)
        print("Master =>", numbers)
        numbers = self.normalize_rpn_to_nines(numbers)
        while len(numbers) > 1:
            numbers = self.calculate(numbers, 1)
            print("Master: ", numbers)

        result = self.cast_to_nines(numbers[0])
        print("R=", result)
            

a = ArimeticAccountant()
m = MasterAritmeticAccountant()
operation = "492 * 61 + 2983"
print("Accountant = ", a.init(operation), m.cast_to_nines(a.init(operation)))
m.init(operation)
        

        
