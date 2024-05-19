from typing import Callable

def memoized_fibonacci() -> Callable[[int], int]:
    cache = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

def main():
    fib_function = memoized_fibonacci()
    print(fib_function(10))
    print(fib_function(15))

if __name__ == "__main__":
    main()
