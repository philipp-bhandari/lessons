class PolishNotation:
    def __init__(self, expr):

        expr = expr.split()

        try:
            self.operator = expr[0]
            self.operand_1 = int(expr[1])
            self.operand_2 = int(expr[2])

            try:
                assert self.operand_1 >= 0 and self.operand_2 >= 0
            except AssertionError:
                self.operand_1 = abs(self.operand_1)
                self.operand_2 = abs(self.operand_2)
                print('\nОперанды преобразованы в положительные числа.\n')

            try:
                assert self.operator in ['+', '-', '*', '/']
            except AssertionError:
                print('\nНеверный оператор. Попробуйте еще раз.\n')
                exit()

        except ValueError:
            print('\nОперанды не являются числами. Попробуйте еще раз.\n')
            exit()

        except IndexError:
            print('Вы ввели мало операндов. Попробуйте еще раз.')
            exit()

    def addition(self):
        return self.operand_1 + self.operand_2

    def subtraction(self):
        return self.operand_1 - self.operand_2

    def multiplication(self):
        return self.operand_1 * self.operand_2

    def division(self):
        try:
            return self.operand_1 / self.operand_2
        except ZeroDivisionError:
            return 'На ноль делить нельзя. Попробуйте еще раз.'


print('\nВведите выражение в польской нотации, '
      'операнды и операторы разделяйте пробелами. '
      'Операции производятся с первыми двумя операндами, '
      'остальные игнорируются\n')

input_str = input()

result = PolishNotation(input_str)

if result.operator == '+':
    result = result.addition()
elif result.operator == '-':
    result = result.subtraction()
elif result.operator == '*':
    result = result.multiplication()
else:
    result = result.division()

print('\nРезультат вычисления: {}\n'.format(result))



