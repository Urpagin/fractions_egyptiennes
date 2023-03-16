from sympy import symbols, solve
from decimal import *


def decomposition(denominator: int, a: int) -> tuple[int, int, int]:
    # a = Reste division
    while True:
        denominator_minus = denominator - a

        if not denominator_minus:
            raise Exception('Dénoninateur nul')

        def get_divider(num: int) -> list[int, ...]:
            dividers = []
            for d in range(2, num):
                if num % d == 0:
                    dividers.append(d)
            return dividers

        x_list = get_divider(denominator_minus)

        if not x_list:
            a += 1
        else:
            x = max(x_list)  # Facteur 1
            y = int(denominator_minus / x)  # Facteur 2
            return a, x, y


# def get_b(a: int, x: int, y: int) -> int:
#     while True:
#         b = symbols('b')
#         eq = -4 / (a + x * y) + 1 / (b + x) + 1 / (a + x * y) + 1 / ((a + x * y) * (b + x))
#         sol = solve(eq, b)
#         result_b = int(sol[0])
#
#         if type(result_b) != int:
#             a += 1
#         else:
#             return result_b

def get_b(a: int, x: int, y: int) -> float:
    while True:
        # b = (3 * x - 1 - a - x * y) / -2
        b = (-3 * x + a + x * y + 1) / 3

        int_b = int(str(b)[-1:])
        if int_b != 0:
            a += 1
        else:
            return b


def get_b_test(a: int, x: int, y: int) -> float:
    pass


def get_frac(a: int, x: int, y: int) -> float:
    # utilise .maths to get perfect no issuee  llzd
    print(f"1/{b + x} + 1/{a + x * y} + 1/{(a + x * y) * (b + x)}")
    return 1 / b + x + 1 / a + x * y + 1 / (a + x * y) * (b + x)


if __name__ == '__main__':
    denominateur = int(input('Dénominateur: '))
    original_a = 1

    a, x, y = decomposition(denominateur, original_a)
    original_a = a
    b = get_b(a, x, y)
    result_frac = get_frac(a, x, y)

    print(f"a: {a}\nx: {x}\ny: {y}\nb: {b}\nfraction: {result_frac}")
