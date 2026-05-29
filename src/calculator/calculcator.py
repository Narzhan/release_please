def add(a: int, b: int) -> int:
    return a + b


def div(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError
    return a / b


def subtract(a: int, b: int) -> int:
    return a - b


def modulo(a: int, b: int) -> int:
    return a % b


def multiply(a: int, b: int) -> int:
    return a * b
