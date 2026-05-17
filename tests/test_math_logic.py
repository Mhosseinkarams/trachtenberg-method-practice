import sys
import os

# Add the app directory to the path so we can import math_logic
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))

from math_logic import (
    gen_tracht_11, gen_tracht_12, gen_tracht_5,
    gen_vedic_square_5, gen_vedic_base_10,
    gen_vedic_squaring_general, gen_vedic_sqrt_perfect,
    gen_tracht_addition, gen_vedic_complementary_addition
)

def test_gen_tracht_11():
    for _ in range(100):
        result = gen_tracht_11()
        assert "11 x" in result["question"]
        num = int(result["question"].split("x")[1].strip())
        assert result["answer"] == 11 * num

def test_gen_tracht_12():
    for _ in range(100):
        result = gen_tracht_12()
        assert "12 x" in result["question"]
        num = int(result["question"].split("x")[1].strip())
        assert result["answer"] == 12 * num

def test_gen_tracht_5():
    for _ in range(100):
        result = gen_tracht_5()
        assert "5 x" in result["question"]
        num = int(result["question"].split("x")[1].strip())
        assert result["answer"] == 5 * num

def test_gen_vedic_square_5():
    for _ in range(100):
        result = gen_vedic_square_5()
        assert "²" in result["question"]
        num = int(result["question"].replace("²", ""))
        assert num % 10 == 5
        assert result["answer"] == num * num

def test_gen_vedic_base_10():
    for _ in range(100):
        result = gen_vedic_base_10()
        assert "x" in result["question"]
        parts = result["question"].split("x")
        a = int(parts[0].strip())
        b = int(parts[1].strip())
        assert result["answer"] == a * b

def test_gen_vedic_squaring_general():
    for _ in range(100):
        result = gen_vedic_squaring_general()
        assert "²" in result["question"]
        num = int(result["question"].replace("²", ""))
        assert result["answer"] == num * num

def test_gen_vedic_sqrt_perfect():
    for _ in range(100):
        result = gen_vedic_sqrt_perfect()
        assert "√" in result["question"]
        num = int(result["question"].replace("√", ""))
        assert result["answer"] * result["answer"] == num

def test_gen_tracht_addition():
    for _ in range(100):
        result = gen_tracht_addition()
        assert "+" in result["question"]
        parts = result["question"].split("+")
        a = int(parts[0].strip())
        b = int(parts[1].strip())
        assert result["answer"] == a + b

def test_gen_vedic_complementary_addition():
    for _ in range(100):
        result = gen_vedic_complementary_addition()
        assert "+" in result["question"]
        parts = result["question"].split("+")
        a = int(parts[0].strip())
        b = int(parts[1].strip())
        assert result["answer"] == a + b
