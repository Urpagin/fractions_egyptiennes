from sympy import symbols, solve
from bigfloat import *
from fractions import Fraction


def decomposition(denominator: int, a: int) -> tuple[int, int, int]:
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


def get_b(a: int, x: int, y: int) -> int:
    b = symbols('b')
    eq = 3 * (b + x) - 1 - a - x * y
    sol = solve(eq, b)
    result_b = float(sol[0])
    return result_b


def get_frac(a: int, x: int, y: int) -> dict:
    results = {
        'addition': f"1/{b + x} + 1/{a + x * y} + 1/{(a + x * y) * (b + x)}",
        # 'simplified': str(Fraction(1, b + x) + Fraction(1, a + x * y) + Fraction(1, (a + x * y) * (b + x))),
    }

    return results


if __name__ == '__main__':
    denominateur = int(input('Dénominateur: '))
    original_a = 1

    a, x, y = decomposition(denominateur, original_a)
    original_a = a
    b = get_b(a, x, y)
    result_frac = get_frac(a, x, y)

    print(f"a: {a}\nx: {x}\ny: {y}\nb: {b}\nfraction: {result_frac.__str__()}")
