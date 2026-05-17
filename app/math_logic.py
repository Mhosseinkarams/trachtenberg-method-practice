import random
import math

class Rule:
    def __init__(self, id, name, description, method, explanation, example, generate_problem_fn):
        self.id = id
        self.name = name
        self.description = description
        self.method = method
        self.explanation = explanation
        self.example = example
        self.generate_problem_fn = generate_problem_fn

    def generate_problem(self):
        return self.generate_problem_fn()

def gen_tracht_11():
    num = random.randint(100, 9099)
    return {"question": f"11 x {num}", "answer": 11 * num}

def gen_tracht_12():
    num = random.randint(100, 9099)
    return {"question": f"12 x {num}", "answer": 12 * num}

def gen_tracht_5():
    num = random.randint(100, 9099)
    return {"question": f"5 x {num}", "answer": 5 * num}

def gen_vedic_square_5():
    base = random.randint(1, 12)
    num = base * 10 + 5
    return {"question": f"{num}²", "answer": num * num}

def gen_vedic_base_10():
    a = random.randint(7, 13)
    b = random.randint(7, 13)
    return {"question": f"{a} x {b}", "answer": a * b}

def gen_vedic_base_100():
    a = random.randint(90, 110)
    b = random.randint(90, 110)
    return {"question": f"{a} x {b}", "answer": a * b}

def gen_vedic_squaring_general():
    num = random.randint(11, 99)
    return {"question": f"{num}²", "answer": num * num}

def gen_vedic_sqrt_perfect():
    root = random.randint(10, 99)
    num = root * root
    return {"question": f"√{num}", "answer": root}

def gen_tracht_addition():
    a = random.randint(100, 999)
    b = random.randint(100, 999)
    return {"question": f"{a} + {b}", "answer": a + b}

def gen_tracht_6():
    num = random.randint(100, 9099)
    return {"question": f"6 x {num}", "answer": 6 * num}

def gen_tracht_7():
    num = random.randint(100, 9099)
    return {"question": f"7 x {num}", "answer": 7 * num}

def gen_tracht_8():
    num = random.randint(100, 9099)
    return {"question": f"8 x {num}", "answer": 8 * num}

def gen_tracht_9():
    num = random.randint(100, 9099)
    return {"question": f"9 x {num}", "answer": 9 * num}

def gen_tracht_4():
    num = random.randint(100, 9099)
    return {"question": f"4 x {num}", "answer": 4 * num}

def gen_tracht_3():
    num = random.randint(100, 9099)
    return {"question": f"3 x {num}", "answer": 3 * num}

def gen_vedic_base_1000():
    a = random.randint(990, 1010)
    b = random.randint(990, 1010)
    return {"question": f"{a} x {b}", "answer": a * b}

def gen_vedic_complementary_addition():
    base = random.randint(1, 8) * 10
    diff = random.randint(1, 9)
    a = base + diff
    b = (10 - diff) + random.randint(0, 4) * 10
    return {"question": f"{a} + {b}", "answer": a + b}

def gen_vedic_subtraction_base():
    base = 10 ** random.randint(1, 3)
    num = random.randint(1, base - 1)
    return {"question": f"{base} - {num}", "answer": base - num}

def gen_vedic_vertically_crosswise():
    a = random.randint(11, 99)
    b = random.randint(11, 99)
    return {"question": f"{a} x {b}", "answer": a * b}

def gen_vedic_square_near_base():
    base = 10 ** random.randint(1, 2)
    diff = random.randint(-5, 5)
    if diff == 0: diff = 1
    num = base + diff
    return {"question": f"{num}²", "answer": num * num}

def gen_tracht_13():
    num = random.randint(100, 9099)
    return {"question": f"13 x {num}", "answer": 13 * num}

def gen_tracht_general():
    a = random.randint(11, 99)
    b = random.randint(11, 99)
    return {"question": f"{a} x {b}", "answer": a * b}

def gen_tracht_division():
    divisor = random.randint(2, 12)
    quotient = random.randint(10, 99)
    num = divisor * quotient
    return {"question": f"{num} ÷ {divisor}", "answer": quotient}

def gen_tracht_sqrt():
    root = random.randint(10, 40)
    num = root * root
    return {"question": f"√{num}", "answer": root}

def gen_vedic_div_9():
    num = random.randint(10, 89)
    return {"question": f"{num} ÷ 9", "answer": num // 9}

def gen_vedic_series_9():
    num = random.randint(11, 99)
    return {"question": f"{num} x 99", "answer": num * 99}

def gen_vedic_ekadhikena():
    base = random.randint(1, 9) * 10
    d1 = random.randint(1, 9)
    d2 = 10 - d1
    a = base + d1
    b = base + d2
    return {"question": f"{a} x {b}", "answer": a * b}

def gen_vedic_cubing():
    base = 10
    diff = random.randint(1, 3)
    num = base + diff
    return {"question": f"{num}³", "answer": num ** 3}

rules = [
    Rule(
        'tracht-11',
        'Multiplication by 11',
        'Add the neighbor rule.',
        'Trachtenberg',
        'To multiply a number by 11: 1. The last digit of the number is the last digit of the answer. 2. Each successive digit of the number is added to its right-hand neighbor. 3. The first digit of the number becomes the first digit of the answer (plus any carry).\n\nCheck: Digit sum(11) * Digit sum(number) = Digit sum(answer).',
        '11 x 432 = 4 (4+3) (3+2) 2 = 4752',
        gen_tracht_11
    ),
    Rule(
        'tracht-12',
        'Multiplication by 12',
        'Double the digit and add the neighbor.',
        'Trachtenberg',
        'To multiply by 12: Double each digit in turn and add its neighbor.\n\nCheck: Digit sum(12) * Digit sum(number) = Digit sum(answer).',
        '12 x 413 = (2*4+1) (2*1+3) (2*3) = 4956',
        gen_tracht_12
    ),
    Rule(
        'tracht-5',
        'Multiplication by 5',
        'Half the neighbor rule.',
        'Trachtenberg',
        'Use half the neighbor: if the digit is odd, add 5 to half the neighbor.\n\nCheck: Digit sum(5) * Digit sum(number) = Digit sum(answer).',
        '5 x 426 = (half of 4) (half of 2) (half of 6) 0 = 2130',
        gen_tracht_5
    ),
    Rule(
        'vedic-square-5',
        'Squaring ending in 5',
        'By one more than the previous one.',
        'Vedic',
        'To square a number ending in 5: Multiply the part before 5 by (itself + 1), then append 25.\n\nCheck: Digit sum(number)² = Digit sum(answer).',
        '35² = (3 * 4) | 25 = 1225',
        gen_vedic_square_5
    ),
    Rule(
        'vedic-base-10',
        'Multiplication near base 10',
        'All from 9 and the last from 10.',
        'Vedic',
        'Multiply numbers close to 10. Find the deficiencies, multiply them for the right part, add crosswise for the left part.\n\nCheck: Casting out nines.',
        '9 x 8: Deficiencies are 1 and 2. 1*2=2. 9-2=7 or 8-1=7. Answer 72.',
        gen_vedic_base_10
    ),
    Rule(
        'vedic-base-100',
        'Multiplication near base 100',
        'Nikhilam Sutra.',
        'Vedic',
        'Multiply numbers close to 100. Find the deficiencies, multiply them for the right part (2 digits), add crosswise for the left part.\n\nCheck: Casting out nines.',
        '97 x 96: Deficiencies 3 and 4. 3*4=12. 97-4=93. Answer 9312.',
        gen_vedic_base_100
    ),
    Rule(
        'vedic-squaring-general',
        'General Squaring',
        'Duplex method.',
        'Vedic',
        'To square any number: use the duplex (D). For a single digit a, D=a^2. For two digits ab, D=2ab.\n\nCheck: Digit sum(number)² = Digit sum(answer).',
        '23² = D(2) | D(23) | D(3) = 4 | 12 | 9 = 529',
        gen_vedic_squaring_general
    ),
    Rule(
        'vedic-sqrt-perfect',
        'Square Root (Perfect)',
        'Observation method.',
        'Vedic',
        'Look at the last digit to find the possible last digit of the root. Ignore last two digits and find the nearest square below the remaining number.\n\nCheck: Result squared should equal original number.',
        'sqrt(1225): ends in 5, so root ends in 100 5. 12 is between 3^2 and 4^2. So tens digit is 3. Answer 35.',
        gen_vedic_sqrt_perfect
    ),
    Rule(
        'tracht-addition',
        'Rapid Addition',
        'The L-R column method.',
        'Trachtenberg',
        'Add columns from left to right, then adjust for carries.\n\nCheck: Sum of digit sums of each number = Digit sum of total.',
        '456 + 123 = (4+1) (5+2) (6+3) = 579',
        gen_tracht_addition
    ),
    Rule(
        'tracht-6',
        'Multiplication by 6',
        'Add half the neighbor rule.',
        'Trachtenberg',
        'To multiply by 6: Add half of the neighbor to each digit. If the digit is odd, add 5.\n\nCheck: Digit sum(6) * Digit sum(number) = Digit sum(answer).',
        '6 x 422 = (4+1) (2+1) (2+0) = 2532',
        gen_tracht_6
    ),
    Rule(
        'tracht-7',
        'Multiplication by 7',
        'Double the digit and add half the neighbor.',
        'Trachtenberg',
        'To multiply by 7: Double each digit and add half of the neighbor. If the digit is odd, add 5.\n\nCheck: Digit sum(7) * Digit sum(number) = Digit sum(answer).',
        '7 x 242 = (2*2+2) (2*4+1) (2*2+0) = 1694',
        gen_tracht_7
    ),
    Rule(
        'tracht-8',
        'Multiplication by 8',
        'Double the complement and add neighbor.',
        'Trachtenberg',
        'To multiply by 8: 1. Rightmost: (10 - digit) * 2. 2. Middle: (9 - digit) * 2 + neighbor. 3. Leftmost: neighbor - 2.\n\nCheck: Digit sum(8) * Digit sum(number) = Digit sum(answer).',
        '8 x 432: (10-2)*2=16; (9-3)*2+2+1=15; (9-4)*2+3+1=14; 4-2+1=3. Ans: 3456',
        gen_tracht_8
    ),
    Rule(
        'tracht-9',
        'Multiplication by 9',
        'Subtract from 10, then from 9.',
        'Trachtenberg',
        'To multiply by 9: 1. Subtract the right-most digit from 10. 2. For other digits, subtract from 9 and add the neighbor. 3. For the leading zero, subtract 1 from the neighbor.\n\nCheck: Result digit sum should be 9.',
        '9 x 432: (10-2=8), (9-3+2=8), (9-4+3=8), (4-1=3) = 3888',
        gen_tracht_9
    ),
    Rule(
        'vedic-base-1000',
        'Multiplication near base 1000',
        'Nikhilam Sutra (Base 1000).',
        'Vedic',
        'Multiply numbers close to 1000. Find deficiencies, multiply them for the right part (3 digits), add crosswise for the left part.\n\nCheck: Casting out nines.',
        '998 x 997: Deficiencies 2 and 3. 2*3=006. 998-3=995. Answer 995006.',
        gen_vedic_base_1000
    ),
    Rule(
        'vedic-complementary-addition',
        'Complementary Addition',
        'Completing the whole.',
        'Vedic',
        'Look for numbers that add up to 10, 100, etc. to simplify addition.\n\nCheck: Sum of digit sums = Digit sum of total.',
        '48 + 32 = 40 + 30 + (8 + 2) = 70 + 10 = 80',
        gen_vedic_complementary_addition
    ),
    Rule(
        'tracht-4',
        'Multiplication by 4',
        'Subtract from 9 and add half of neighbor.',
        'Trachtenberg',
        'To multiply by 4: 1. Subtract the right-most digit from 10, add 5 if the digit is odd. 2. For other digits, subtract from 9, add half the neighbor, and add 5 if the digit is odd. 3. Leading zero: half the neighbor minus 1.\n\nCheck: Digit sum(4) * Digit sum(number) = Digit sum(answer).',
        '4 x 426: (10-6=4), (9-2+3=10, 1 carry), (9-4+1+1=7), (2-1=1). Answer 1704',
        gen_tracht_4
    ),
    Rule(
        'tracht-3',
        'Multiplication by 3',
        'Two-times the complement and add half neighbor.',
        'Trachtenberg',
        'To multiply by 3: 1. Rightmost: Subtract from 10, double, add 5 if odd. 2. Middle: Subtract from 9, double, add half the neighbor, add 5 if odd. 3. Leftmost: Half the neighbor minus 2.\n\nCheck: Digit sum(3) * Digit sum(number) = Digit sum(answer).',
        '3 x 422: (10-2)*2=16; (9-2)*2+1+1=16; (9-4)*2+1+1=12; 2-2+1=1. Ans: 1266',
        gen_tracht_3
    ),
    Rule(
        'vedic-subtraction-base',
        'Subtraction from Base',
        'All from 9 and the last from 10.',
        'Vedic',
        'To subtract a number from a power of 10: Subtract each digit from 9, and the last (non-zero) digit from 10.\n\nCheck: Answer + Number = Base.',
        '1000 - 456 = (9-4) (9-5) (10-6) = 544',
        gen_vedic_subtraction_base
    ),
    Rule(
        'vedic-vertically-crosswise',
        'Vertically and Crosswise',
        'Urdhva Tiryagbhyam Sutra.',
        'Vedic',
        'Multiply 2-digit numbers: 1. Multiply the units (right column). 2. Cross-multiply and add. 3. Multiply the tens (left column). Carry where necessary.\n\nCheck: Casting out nines.',
        '23 x 12: (2*1) | (2*2 + 3*1) | (3*2) = 2 | 7 | 6 = 276',
        gen_vedic_vertically_crosswise
    ),
    Rule(
        'vedic-square-near-base',
        'Squaring near Base',
        'Yavadunam Sutra.',
        'Vedic',
        'To square a number near a base (10, 100): 1. Left part: Number + Deficiency. 2. Right part: Deficiency squared.\n\nCheck: Digit sum(number)² = Digit sum(answer).',
        '13²: Base 10, diff +3. (13+3) | (3²) = 16 | 9 = 169',
        gen_vedic_square_near_base
    ),
    Rule(
        'tracht-13',
        'Multiplication by 13',
        'Triple the digit and add the neighbor.',
        'Trachtenberg',
        'To multiply by 13: Triple each digit in turn and add its neighbor.\n\nCheck: Casting out nines (Digit sum). Sum the digits of the result. It should equal the digit sum of (1 + 3) * digit sum of the number.',
        '13 x 12 = (3*0+1) (3*1+2) (3*2) = 156.',
        gen_tracht_13
    ),
    Rule(
        'tracht-general',
        'General Multiplication',
        'Two-finger method.',
        'Trachtenberg',
        'Direct multiplication without tables. Use the "Outside-Inside" rule: multiply the outside pair and the inside pair and add. Repeat for each position.\n\nCheck: Casting out nines (Digit sum).',
        '23 x 12 = (2*1) | (2*2 + 3*1) | (3*2) = 276',
        gen_tracht_general
    ),
    Rule(
        'tracht-division',
        'Direct Division',
        'Speed and accuracy method.',
        'Trachtenberg',
        'Divide using the leading digit of the divisor, then subtract the results of subsequent products from the remainder.\n\nCheck: Multiplication of result and divisor should equal original number.',
        '156 ÷ 12 = 13',
        gen_tracht_division
    ),
    Rule(
        'tracht-sqrt',
        'Square Root',
        'Systematic extraction.',
        'Trachtenberg',
        'Extract digits using the systematic "work back" method based on the nearest square and remainders.\n\nCheck: Result squared should equal original number.',
        '√625 = 25',
        gen_tracht_sqrt
    ),
    Rule(
        'vedic-div-9',
        'Division by 9',
        'Nikilam addition method.',
        'Vedic',
        'The first digit is the first digit of the quotient. Successively add digits for subsequent quotient digits and the final remainder.\n\nCheck: Result * 9 + Remainder = Number.',
        '23 ÷ 9 = 2 R 5',
        gen_vedic_div_9
    ),
    Rule(
        'vedic-series-9',
        'Multiplication by Series of 9s',
        'By one less than the previous one.',
        'Vedic',
        'Subtract 1 from the number for the left part, then subtract the number from the base (all from 9, last from 10) for the right part.\n\nCheck: Casting out nines.',
        '43 x 99 = (43-1) | (100-43) = 4257',
        gen_vedic_series_9
    ),
    Rule(
        'vedic-ekadhikena',
        'Units add to 10',
        'Ekadhikena Purvena.',
        'Vedic',
        'If the tens digits are same and units sum to 10: Multiply tens by (tens + 1) for left part, multiply units for right part.\n\nCheck: Casting out nines.',
        '42 x 48 = (4*5) | (2*8) = 2016',
        gen_vedic_ekadhikena
    ),
    Rule(
        'vedic-cubing',
        'Cubing near Base',
        'Yavadunam (Cubing).',
        'Vedic',
        'To cube a number near base 10: 1. Left: Number + 2*Diff. 2. Middle: 3*Diff^2. 3. Right: Diff^3.\n\nCheck: Digit sum(number)³ = Digit sum(answer).',
        '12³: Base 10, diff 2. (12+4) | (3*4) | (8) = 16 | 12 | 8 = 1728',
        gen_vedic_cubing
    )
]

rules_by_method = {
    "Trachtenberg": [r for r in rules if r.method == "Trachtenberg"],
    "Vedic": [r for r in rules if r.method == "Vedic"]
}
