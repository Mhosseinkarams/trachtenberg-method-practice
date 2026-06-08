import time
import random
from app.math_logic import to_persian_digits

def benchmark_to_persian_digits(iterations=100000):
    start = time.time()
    for i in range(iterations):
        to_persian_digits(i)
    end = time.time()
    print(f"Original to_persian_digits: {end - start:.4f}s for {iterations} calls")

# Improved version
_ENGLISH_DIGITS = "0123456789"
_PERSIAN_DIGITS = "۰۱۲۳۴۵۶۷۸۹"
_PERSIAN_TRANS = str.maketrans(_ENGLISH_DIGITS, _PERSIAN_DIGITS)

def to_persian_digits_optimized(n):
    return str(n).translate(_PERSIAN_TRANS)

def benchmark_to_persian_digits_optimized(iterations=100000):
    start = time.time()
    for i in range(iterations):
        to_persian_digits_optimized(i)
    end = time.time()
    print(f"Optimized to_persian_digits: {end - start:.4f}s for {iterations} calls")

if __name__ == "__main__":
    benchmark_to_persian_digits()
    benchmark_to_persian_digits_optimized()
