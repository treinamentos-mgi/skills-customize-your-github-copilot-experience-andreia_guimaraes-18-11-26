def add(left: int, right: int) -> int:
    return left + right


def is_even(value: int) -> bool:
    return value % 2 == 0


def average(values: list[int | float]) -> float:
    if not values:
        raise ValueError("Cannot calculate the average of an empty list")
    return sum(values) / len(values)


def divide(numerator: int | float, denominator: int | float) -> float:
    if denominator == 0:
        raise ValueError("Cannot divide by zero")
    return numerator / denominator
