import re
from decimal import Decimal
from typing import Callable, Generator


def decimal_generator(text: str) -> Generator[Decimal, None, None]:
    for word in text.split():
        if re.match(r"\d+\.\d+", word):
            yield Decimal(word)


def calculate_sum(text: str, generator_func: Callable[[str], Generator[Decimal, None, None]]) -> Decimal:
    return sum(generator_func(text))


def main():
    text_data = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 i 324.00 доларів."
    total_income = calculate_sum(text_data, decimal_generator)
    print(f"Загальний дохід: {total_income}")


if __name__ == "__main__":
    main()
