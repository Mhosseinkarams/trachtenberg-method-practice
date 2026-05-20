import random
import math

# Pre-calculate powers of 10 for performance optimization in problem generators
POWERS_OF_10 = [10**i for i in range(10)]

def to_persian_digits(n):
    n = str(n)
    english_digits = "0123456789"
    persian_digits = "۰۱۲۳۴۵۶۷۸۹"
    translation_table = str.maketrans(english_digits, persian_digits)
    return n.translate(translation_table)

def to_lang_digits(n, lang):
    if lang == 'fa':
        return to_persian_digits(n)
    return str(n)

class Rule:
    def __init__(self, id, names, descriptions, category, method, explanations, examples, generate_problem_fn, steps_fn=None):
        self.id = id
        self.names = names  # {'en': '...', 'fa': '...'}
        self.descriptions = descriptions
        self.category = category
        self.method = method
        self.explanations = explanations
        self.examples = examples
        self.generate_problem_fn = generate_problem_fn
        self.steps_fn = steps_fn

    def get_name(self, lang):
        return self.names.get(lang, self.names.get('en', ''))

    def get_description(self, lang):
        return self.descriptions.get(lang, self.descriptions.get('en', ''))

    def get_explanation(self, lang):
        return self.explanations.get(lang, self.explanations.get('en', ''))

    def get_example(self, lang):
        return self.examples.get(lang, self.examples.get('en', ''))

    def generate_problem(self, **kwargs):
        return self.generate_problem_fn(**kwargs)

    def get_steps(self, problem, lang):
        if self.steps_fn:
            return self.steps_fn(problem, lang)
        return []

# Problem Generators
def gen_tracht_11(**kwargs):
    num = random.randint(100, 9099)
    return {"question": f"11 x {num}", "answer": 11 * num, "num": num}

def gen_tracht_12(**kwargs):
    num = random.randint(100, 9099)
    return {"question": f"12 x {num}", "answer": 12 * num, "num": num}

def gen_tracht_5(**kwargs):
    num = random.randint(100, 9099)
    return {"question": f"5 x {num}", "answer": 5 * num, "num": num}

def gen_tracht_6(**kwargs):
    num = random.randint(100, 9099)
    return {"question": f"6 x {num}", "answer": 6 * num, "num": num}

def gen_tracht_7(**kwargs):
    num = random.randint(100, 9099)
    return {"question": f"7 x {num}", "answer": 7 * num, "num": num}

def gen_tracht_8(**kwargs):
    num = random.randint(100, 9099)
    return {"question": f"8 x {num}", "answer": 8 * num, "num": num}

def gen_tracht_9(**kwargs):
    num = random.randint(100, 9099)
    return {"question": f"9 x {num}", "answer": 9 * num, "num": num}

def gen_tracht_4(**kwargs):
    num = random.randint(100, 9099)
    return {"question": f"4 x {num}", "answer": 4 * num, "num": num}

def gen_tracht_3(**kwargs):
    num = random.randint(100, 9099)
    return {"question": f"3 x {num}", "answer": 3 * num, "num": num}

def gen_tracht_13(**kwargs):
    num = random.randint(100, 9099)
    return {"question": f"13 x {num}", "answer": 13 * num, "num": num}

def gen_tracht_general(**kwargs):
    a = random.randint(11, 99)
    b = random.randint(11, 99)
    return {"question": f"{a} x {b}", "answer": a * b, "a": a, "b": b}

def gen_tracht_addition(num_operands=2, num_digits=3, **kwargs):
    operands = []
    for _ in range(num_operands):
        if num_digits == 0: # 0 means random
            d = random.randint(1, 6)
        else:
            d = num_digits
        operands.append(random.randint(POWERS_OF_10[d-1], POWERS_OF_10[d] - 1))
    question = " + ".join(map(str, operands))
    answer = sum(operands)
    return {"question": question, "answer": answer, "operands": operands}

def gen_tracht_division(**kwargs):
    divisor = random.randint(2, 12)
    quotient = random.randint(10, 99)
    num = divisor * quotient
    return {"question": f"{num} ÷ {divisor}", "answer": quotient, "num": num, "divisor": divisor}

def gen_tracht_sqrt(**kwargs):
    root = random.randint(10, 40)
    num = root * root
    return {"question": f"√{num}", "answer": root, "num": num}

def gen_vedic_square_5(**kwargs):
    base = random.randint(1, 12)
    num = base * 10 + 5
    return {"question": f"{num}²", "answer": num * num, "num": num}

def gen_vedic_base_10(**kwargs):
    a = random.randint(7, 13)
    b = random.randint(7, 13)
    return {"question": f"{a} x {b}", "answer": a * b, "a": a, "b": b}

def gen_vedic_base_100(**kwargs):
    a = random.randint(90, 110)
    b = random.randint(90, 110)
    return {"question": f"{a} x {b}", "answer": a * b, "a": a, "b": b}

def gen_vedic_base_1000(**kwargs):
    a = random.randint(990, 1010)
    b = random.randint(990, 1010)
    return {"question": f"{a} x {b}", "answer": a * b, "a": a, "b": b}

def gen_vedic_squaring_general(**kwargs):
    num = random.randint(11, 99)
    return {"question": f"{num}²", "answer": num * num, "num": num}

def gen_vedic_sqrt_perfect(**kwargs):
    root = random.randint(10, 99)
    num = root * root
    return {"question": f"√{num}", "answer": root, "num": num}

def gen_vedic_complementary_addition(num_operands=2, num_digits=3, **kwargs):
    if num_operands > 2 or num_digits != 3:
        return gen_tracht_addition(num_operands=num_operands, num_digits=num_digits)
    base = random.randint(1, 8) * 10
    diff = random.randint(1, 9)
    a = base + diff
    b = (10 - diff) + random.randint(0, 4) * 10
    return {"question": f"{a} + {b}", "answer": a + b, "a": a, "b": b}

def gen_vedic_subtraction_base(num_digits=3, **kwargs):
    if num_digits == 0:
        d = random.randint(1, 6)
    else:
        d = num_digits
    base = POWERS_OF_10[d]
    num = random.randint(POWERS_OF_10[d-1], base - 1)
    return {"question": f"{base} - {num}", "answer": base - num, "base": base, "num": num}

def gen_vedic_vertically_crosswise(**kwargs):
    a = random.randint(11, 99)
    b = random.randint(11, 99)
    return {"question": f"{a} x {b}", "answer": a * b, "a": a, "b": b}

def gen_vedic_square_near_base(**kwargs):
    base = 10 ** random.randint(1, 2)
    diff = random.randint(-5, 5)
    if diff == 0: diff = 1
    num = base + diff
    return {"question": f"{num}²", "answer": num * num, "num": num, "base": base}

def gen_vedic_div_9(**kwargs):
    num = random.randint(10, 89)
    return {"question": f"{num} ÷ 9", "answer": num // 9, "num": num}

def gen_vedic_series_9(**kwargs):
    num = random.randint(11, 99)
    return {"question": f"{num} x 99", "answer": num * 99, "num": num}

def gen_vedic_ekadhikena(**kwargs):
    base = random.randint(1, 9) * 10
    d1 = random.randint(1, 9)
    d2 = 10 - d1
    a = base + d1
    b = base + d2
    return {"question": f"{a} x {b}", "answer": a * b, "a": a, "b": b}

def gen_vedic_cubing(**kwargs):
    base = 10
    diff = random.randint(1, 3)
    num = base + diff
    return {"question": f"{num}³", "answer": num ** 3, "num": num}

# Step Functions
def steps_tracht_11(p, lang):
    num_str = str(p['num'])
    steps = []
    if lang == 'en':
        steps.append(f"1. The last digit {num_str[-1]} is the last digit of the answer.")
        for i in range(len(num_str)-1, 0, -1):
            steps.append(f"2. Add {num_str[i]} to its neighbor {num_str[i-1]}: {int(num_str[i])+int(num_str[i-1])}")
        steps.append(f"3. The first digit {num_str[0]} is the first digit of the answer (plus any carry).")
    else:
        steps.append(f"۱. آخرین رقم {to_persian_digits(num_str[-1])} آخرین رقم جواب است.")
        for i in range(len(num_str)-1, 0, -1):
            steps.append(f"۲. رقم {to_persian_digits(num_str[i])} را با همسایه خود {to_persian_digits(num_str[i-1])} جمع کنید: {to_persian_digits(int(num_str[i])+int(num_str[i-1]))}")
        steps.append(f"۳. اولین رقم {to_persian_digits(num_str[0])} اولین رقم جواب است (به اضافه هر رقم نقلی).")
    return steps

def steps_tracht_mul(p, lang, multiplier):
    num_str = "0" + str(p['num'])
    steps = []
    if lang == 'en':
        steps.append(f"Problem: {multiplier} × {p['num']}")
        if multiplier == 12:
            for i in range(len(num_str)-1, 0, -1):
                steps.append(f"Digit {num_str[i]}: ({num_str[i]} × 2) + neighbor {num_str[i+1] if i+1 < len(num_str) else 0}")
        elif multiplier == 5:
            for i in range(len(num_str)-1, 0, -1):
                steps.append(f"Digit {num_str[i]}: Half of neighbor {num_str[i+1] if i+1 < len(num_str) else 0} {'+ 5 (because digit is odd)' if int(num_str[i])%2 else ''}")
    else:
        steps.append(f"مسئله: {to_persian_digits(multiplier)} × {to_persian_digits(p['num'])}")
        if multiplier == 12:
            for i in range(len(num_str)-1, 0, -1):
                neighbor = num_str[i+1] if i+1 < len(num_str) else 0
                steps.append(f"رقم {to_persian_digits(num_str[i])}: ({to_persian_digits(num_str[i])} × ۲) + همسایه {to_persian_digits(neighbor)}")
    if not steps or len(steps) == 1:
        return steps_simple_mul(p, lang)
    return steps

def steps_vedic_square_5(p, lang):
    num = p['num']
    before_5 = num // 10
    steps = []
    if lang == 'en':
        steps.append(f"1. Part before 5 is {before_5}.")
        steps.append(f"2. Multiply {before_5} by its successor ({before_5} + 1 = {before_5 + 1}): {before_5} × {before_5 + 1} = {before_5 * (before_5 + 1)}")
        steps.append(f"3. Append 25 to the result: {before_5 * (before_5 + 1)}|25 = {num * num}")
    else:
        steps.append(f"۱. قسمت قبل از ۵ عدد {to_persian_digits(before_5)} است.")
        steps.append(f"۲. {to_persian_digits(before_5)} را در عدد بعدی‌اش ضرب کنید ({to_persian_digits(before_5)} + ۱ = {to_persian_digits(before_5 + 1)}): {to_persian_digits(before_5)} × {to_persian_digits(before_5 + 1)} = {to_persian_digits(before_5 * (before_5 + 1))}")
        steps.append(f"۳. عدد ۲۵ را به انتهای نتیجه اضافه کنید: {to_persian_digits(num * num)}")
    return steps

def steps_vedic_series_9(p, lang):
    num = p['num']
    steps = []
    if lang == 'en':
        steps.append(f"1. Subtract 1 from {num}: {num} - 1 = {num - 1} (Left part).")
        steps.append(f"2. Subtract {num} from 100: 100 - {num} = {100 - num} (Right part).")
        steps.append(f"Result: {num - 1}{100 - num}")
    else:
        steps.append(f"۱. عدد ۱ را از {to_persian_digits(num)} کم کنید: {to_persian_digits(num)} - ۱ = {to_persian_digits(num - 1)} (بخش چپ).")
        steps.append(f"۲. {to_persian_digits(num)} را از ۱۰۰ کم کنید: ۱۰۰ - {to_persian_digits(num)} = {to_persian_digits(100 - num)} (بخش راست).")
        steps.append(f"نتیجه: {to_persian_digits(num * 99)}")
    return steps

def steps_vedic_sub_base(p, lang):
    base, num = p['base'], p['num']
    steps = []
    if lang == 'en':
        steps.append(f"Problem: {base} - {num}")
        steps.append("1. Subtract each digit from 9, except the last one.")
        steps.append("2. Subtract the last non-zero digit from 10.")
    else:
        steps.append(f"مسئله: {to_persian_digits(base)} - {to_persian_digits(num)}")
        steps.append("۱. تمام ارقام را از ۹ کم کنید، به جز رقم آخر.")
        steps.append("۲. آخرین رقم غیر صفر را از ۱۰ کم کنید.")
    return steps

def steps_vedic_ekadhikena(p, lang):
    a, b = p['a'], p['b']
    tens = a // 10
    u1, u2 = a % 10, b % 10
    steps = []
    if lang == 'en':
        steps.append(f"1. Tens digits are the same ({tens}). Units sum to 10 ({u1}+{u2}=10).")
        steps.append(f"2. Multiply tens by its successor: {tens} × {tens+1} = {tens*(tens+1)} (Left part).")
        steps.append(f"3. Multiply units: {u1} × {u2} = {u1*u2} (Right part).")
    else:
        steps.append(f"۱. دهگان‌ها یکسان هستند ({to_persian_digits(tens)}). مجموع یکان‌ها ۱۰ است.")
        steps.append(f"۲. دهگان را در عدد بعدی‌اش ضرب کنید: {to_persian_digits(tens)} × {to_persian_digits(tens+1)} = {to_persian_digits(tens*(tens+1))} (بخش چپ).")
        steps.append(f"۳. یکان‌ها را در هم ضرب کنید: {to_persian_digits(u1)} × {to_persian_digits(u2)} = {to_persian_digits(u1*u2)} (بخش راست).")
    return steps

def steps_simple_mul(p, lang):
    steps = []
    q = p['question']
    if lang == 'en':
        steps.append(f"Problem: {q}")
        steps.append("Apply the rule mentioned in the explanation above to solve this specific problem step-by-step.")
    else:
        steps.append(f"مسئله: {to_persian_digits(q)}")
        steps.append("قوانین ذکر شده در بخش تئوری بالا را برای حل مرحله‌به‌مرحله این مسئله به کار ببرید.")
    return steps

def steps_vedic_base(p, lang):
    a, b = p['a'], p['b']
    base = 10 if a < 20 else (100 if a < 200 else 1000)
    d_a, d_b = base - a, base - b
    steps = []
    if lang == 'en':
        steps.append(f"1. Base is {base}. Deficiencies are {d_a} and {d_b}.")
        steps.append(f"2. Multiply deficiencies: {d_a} × {d_b} = {d_a * d_b} (Right part).")
        steps.append(f"3. Subtract crosswise: {a} - {d_b} = {a - d_b} (Left part).")
        steps.append(f"Result: {a - d_b}{d_a * d_b if d_a * d_b >= 10 or base==10 else '0'+str(d_a*d_b)}")
    else:
        steps.append(f"۱. مبنا {to_persian_digits(base)} است. اختلاف‌ها {to_persian_digits(d_a)} و {to_persian_digits(d_b)} هستند.")
        steps.append(f"۲. حاصل‌ضرب اختلاف‌ها: {to_persian_digits(d_a)} × {to_persian_digits(d_b)} = {to_persian_digits(d_a * d_b)} (بخش راست).")
        steps.append(f"۳. تفریق متقاطع: {to_persian_digits(a)} - {to_persian_digits(d_b)} = {to_persian_digits(a - d_b)} (بخش چپ).")
    return steps

rules = [
    Rule(
        'tracht-11',
        {'en': 'Multiplication by 11', 'fa': 'ضرب اعداد در ۱۱'},
        {'en': 'Add the neighbor rule.', 'fa': 'قانون اضافه کردن همسایه.'},
        'Multiplication', 'Trachtenberg',
        {
            'en': 'To multiply by 11: 1. Last digit is last. 2. Add each digit to its neighbor. 3. First digit is first.',
            'fa': 'برای ضرب در ۱۱: ۱. رقم آخر خودش است. ۲. هر رقم را با همسایه‌اش جمع کنید. ۳. رقم اول خودش است.'
        },
        {'en': '11 x 432 = 4752', 'fa': '۱۱ × ۴۳۲ = ۴۷۵۲'},
        gen_tracht_11, steps_tracht_11
    ),
    Rule(
        'tracht-12',
        {'en': 'Multiplication by 12', 'fa': 'ضرب اعداد در ۱۲'},
        {'en': 'Double the digit and add neighbor.', 'fa': 'رقم را دو برابر کرده و با همسایه جمع کنید.'},
        'Multiplication', 'Trachtenberg',
        {
            'en': 'To multiply by 12: Double each digit and add its neighbor.',
            'fa': 'برای ضرب در ۱۲: هر رقم را دو برابر کرده و با همسایه‌اش جمع کنید.'
        },
        {'en': '12 x 413 = 4956', 'fa': '۱۲ × ۴۱۳ = ۴۹۵۶'},
        gen_tracht_12, lambda p, l: steps_tracht_mul(p, l, 12)
    ),
    Rule(
        'tracht-5',
        {'en': 'Multiplication by 5', 'fa': 'ضرب اعداد در ۵'},
        {'en': 'Half the neighbor rule.', 'fa': 'قانون نصف همسایه.'},
        'Multiplication', 'Trachtenberg',
        {
            'en': 'Use half the neighbor: if the digit is odd, add 5 to half the neighbor.',
            'fa': 'از نصف همسایه استفاده کنید: اگر رقم فرد است، ۵ را به نصف همسایه اضافه کنید.'
        },
        {'en': '5 x 426 = 2130', 'fa': '۵ × ۴۲۶ = ۲۱۳۰'},
        gen_tracht_5, lambda p, l: steps_tracht_mul(p, l, 5)
    ),
    Rule(
        'tracht-6',
        {'en': 'Multiplication by 6', 'fa': 'ضرب اعداد در ۶'},
        {'en': 'Add half the neighbor rule.', 'fa': 'قانون اضافه کردن نصف همسایه.'},
        'Multiplication', 'Trachtenberg',
        {
            'en': 'To multiply by 6: Add half of the neighbor. If odd, add 5.',
            'fa': 'برای ضرب در ۶: نصف همسایه را اضافه کنید. اگر فرد است ۵ واحد اضافه کنید.'
        },
        {'en': '6 x 422 = 2532', 'fa': '۶ × ۴۲۲ = ۲۵۳۲'},
        gen_tracht_6, steps_simple_mul
    ),
    Rule(
        'tracht-7',
        {'en': 'Multiplication by 7', 'fa': 'ضرب اعداد در ۷'},
        {'en': 'Double the digit and add half neighbor.', 'fa': 'رقم را دو برابر کرده و با نصف همسایه جمع کنید.'},
        'Multiplication', 'Trachtenberg',
        {
            'en': 'To multiply by 7: Double each digit and add half of the neighbor. If odd, add 5.',
            'fa': 'برای ضرب در ۷: هر رقم را دو برابر کرده و با نصف همسایه جمع کنید. اگر فرد است ۵ واحد اضافه کنید.'
        },
        {'en': '7 x 242 = 1694', 'fa': '۷ × ۲۴۲ = ۱۶۹۴'},
        gen_tracht_7, steps_simple_mul
    ),
    Rule(
        'tracht-8',
        {'en': 'Multiplication by 8', 'fa': 'ضرب اعداد در ۸'},
        {'en': 'Double the complement and add neighbor.', 'fa': 'دو برابر متمم و جمع با همسایه.'},
        'Multiplication', 'Trachtenberg',
        {
            'en': 'To multiply by 8: 1. Rightmost: (10-digit)*2. 2. Middle: (9-digit)*2+neighbor. 3. Leftmost: neighbor-2.',
            'fa': 'برای ضرب در ۸: ۱. راست‌ترین: ۲ × (۱۰-رقم). ۲. میانی: (۲ × (۹-رقم)) + همسایه. ۳. چپ‌ترین: همسایه - ۲.'
        },
        {'en': '8 x 432 = 3456', 'fa': '۸ × ۴۳۲ = ۳۴۵۶'},
        gen_tracht_8, steps_simple_mul
    ),
    Rule(
        'tracht-9',
        {'en': 'Multiplication by 9', 'fa': 'ضرب اعداد در ۹'},
        {'en': 'Subtract from 10, then from 9.', 'fa': 'تفریق از ۱۰، سپس از ۹.'},
        'Multiplication', 'Trachtenberg',
        {
            'en': 'To multiply by 9: 1. Rightmost from 10. 2. Others from 9 and add neighbor. 3. Leading zero: neighbor-1.',
            'fa': 'برای ضرب در ۹: ۱. راست‌ترین از ۱۰. ۲. بقیه از ۹ و جمع با همسایه. ۳. صفر پیشرو: همسایه منهای ۱.'
        },
        {'en': '9 x 432 = 3888', 'fa': '۹ × ۴۳۲ = ۳۸۸۸'},
        gen_tracht_9, steps_simple_mul
    ),
    Rule(
        'tracht-4',
        {'en': 'Multiplication by 4', 'fa': 'ضرب اعداد در ۴'},
        {'en': 'Subtract from 9 and add half of neighbor.', 'fa': 'تفریق از ۹ و جمع با نصف همسایه.'},
        'Multiplication', 'Trachtenberg',
        {
            'en': 'To multiply by 4: Subtract from 9, add half neighbor, add 5 if odd.',
            'fa': 'برای ضرب در ۴: از ۹ کم کنید، با نصف همسایه جمع کنید و اگر فرد است ۵ واحد اضافه کنید.'
        },
        {'en': '4 x 426 = 1704', 'fa': '۴ × ۴۲۶ = ۱۷۰۴'},
        gen_tracht_4, steps_simple_mul
    ),
    Rule(
        'tracht-3',
        {'en': 'Multiplication by 3', 'fa': 'ضرب اعداد در ۳'},
        {'en': 'Two-times the complement and add half neighbor.', 'fa': 'دو برابر متمم و جمع با نصف همسایه.'},
        'Multiplication', 'Trachtenberg',
        {
            'en': 'To multiply by 3: Double complement, add half neighbor, add 5 if odd.',
            'fa': 'برای ضرب در ۳: متمم را دو برابر کنید، با نصف همسایه جمع کنید و اگر فرد است ۵ واحد اضافه کنید.'
        },
        {'en': '3 x 422 = 1266', 'fa': '۳ × ۴۲۲ = ۱۲۶۶'},
        gen_tracht_3, steps_simple_mul
    ),
    Rule(
        'tracht-13',
        {'en': 'Multiplication by 13', 'fa': 'ضرب اعداد در ۱۳'},
        {'en': 'Triple the digit and add neighbor.', 'fa': 'رقم را سه برابر کرده و با همسایه جمع کنید.'},
        'Multiplication', 'Trachtenberg',
        {
            'en': 'To multiply by 13: Triple each digit and add its neighbor.',
            'fa': 'برای ضرب در ۱۳: هر رقم را سه برابر کرده و با همسایه‌اش جمع کنید.'
        },
        {'en': '13 x 12 = 156', 'fa': '۱۳ × ۱۲ = ۱۵۶'},
        gen_tracht_13, steps_simple_mul
    ),
    Rule(
        'tracht-general',
        {'en': 'General Multiplication', 'fa': 'ضرب عمومی'},
        {'en': 'Two-finger method.', 'fa': 'روش دو انگشتی.'},
        'Multiplication', 'Trachtenberg',
        {
            'en': 'Direct multiplication without tables. Use the "Outside-Inside" rule.',
            'fa': 'ضرب مستقیم بدون جدول. از قانون "بیرون-درون" استفاده کنید.'
        },
        {'en': '23 x 12 = 276', 'fa': '۲۳ × ۱۲ = ۲۷۶'},
        gen_tracht_general, steps_simple_mul
    ),
    Rule(
        'tracht-addition',
        {'en': 'Rapid Addition', 'fa': 'جمع سریع'},
        {'en': 'The L-R column method.', 'fa': 'روش ستونی چپ به راست.'},
        'Addition & Subtraction', 'Trachtenberg',
        {
            'en': 'Add columns from left to right, then adjust for carries.',
            'fa': 'ستون‌ها را از چپ به راست جمع کنید، سپس رقم‌های نقلی را تنظیم کنید.'
        },
        {'en': '456 + 123 = 579', 'fa': '۴۵۶ + ۱۲۳ = ۵۷۹'},
        gen_tracht_addition, steps_simple_mul
    ),
    Rule(
        'tracht-division',
        {'en': 'Direct Division', 'fa': 'تقسیم مستقیم'},
        {'en': 'Speed and accuracy method.', 'fa': 'روش سرعت و دقت.'},
        'Division & Roots', 'Trachtenberg',
        {
            'en': 'Divide using the leading digit, then subtract cross-products.',
            'fa': 'با استفاده از رقم اول تقسیم کنید و سپس حاصل‌ضرب‌های متقاطع را کم کنید.'
        },
        {'en': '156 ÷ 12 = 13', 'fa': '۱۵۶ ÷ ۱۲ = ۱۳'},
        gen_tracht_division, steps_simple_mul
    ),
    Rule(
        'tracht-sqrt',
        {'en': 'Square Root', 'fa': 'جذر'},
        {'en': 'Systematic extraction.', 'fa': 'استخراج سیستماتیک.'},
        'Division & Roots', 'Trachtenberg',
        {
            'en': 'Extract digits using systematic "work back" method.',
            'fa': 'ارقام را با استفاده از روش سیستماتیک "محاسبه معکوس" استخراج کنید.'
        },
        {'en': '√625 = 25', 'fa': 'جذر ۶۲۵ = ۲۵'},
        gen_tracht_sqrt, steps_simple_mul
    ),
    Rule(
        'vedic-square-5',
        {'en': 'Squaring ending in 5', 'fa': 'مربع اعداد مختوم به ۵'},
        {'en': 'By one more than the previous one.', 'fa': 'با یکی بیشتر از قبلی.'},
        'Squaring & Cubing', 'Vedic',
        {
            'en': 'Multiply the part before 5 by (itself + 1), then append 25.',
            'fa': 'قسمت قبل از ۵ را در (خودش + ۱) ضرب کنید، سپس ۲۵ را به انتها اضافه کنید.'
        },
        {'en': '35² = 1225', 'fa': '۳۵² = ۱۲۲۵'},
        gen_vedic_square_5, steps_vedic_square_5
    ),
    Rule(
        'vedic-base-10',
        {'en': 'Multiplication near base 10', 'fa': 'ضرب نزدیک به مبنای ۱۰'},
        {'en': 'All from 9 and the last from 10.', 'fa': 'همه از ۹ و آخرین از ۱۰.'},
        'Multiplication', 'Vedic',
        {
            'en': 'Find deficiencies, multiply them for right part, add crosswise for left part.',
            'fa': 'اختلاف‌ها را پیدا کنید، برای بخش راست ضرب کنید و برای بخش چپ متقاطع جمع کنید.'
        },
        {'en': '9 x 8 = 72', 'fa': '۹ × ۸ = ۷۲'},
        gen_vedic_base_10, steps_vedic_base
    ),
    Rule(
        'vedic-base-100',
        {'en': 'Multiplication near base 100', 'fa': 'ضرب نزدیک به مبنای ۱۰۰'},
        {'en': 'Nikhilam Sutra.', 'fa': 'نیکیلام سوترا.'},
        'Multiplication', 'Vedic',
        {
            'en': 'Find deficiencies, multiply for right (2 digits), add crosswise for left.',
            'fa': 'اختلاف‌ها را پیدا کنید، برای بخش راست (۲ رقم) ضرب و برای بخش چپ متقاطع جمع کنید.'
        },
        {'en': '97 x 96 = 9312', 'fa': '۹۷ × ۹۶ = ۹۳۱۲'},
        gen_vedic_base_100, steps_vedic_base
    ),
    Rule(
        'vedic-base-1000',
        {'en': 'Multiplication near base 1000', 'fa': 'ضرب نزدیک به مبنای ۱۰۰۰'},
        {'en': 'Nikhilam Sutra (Base 1000).', 'fa': 'نیکیلام سوترا (مبنای ۱۰۰۰).'},
        'Multiplication', 'Vedic',
        {
            'en': 'Find deficiencies, multiply for right (3 digits), add crosswise for left.',
            'fa': 'اختلاف‌ها را پیدا کنید، برای بخش راست (۳ رقم) ضرب و برای بخش چپ متقاطع جمع کنید.'
        },
        {'en': '998 x 997 = 995006', 'fa': '۹۹۸ × ۹۹۷ = ۹۹۵۰۰۶'},
        gen_vedic_base_1000, steps_vedic_base
    ),
    Rule(
        'vedic-squaring-general',
        {'en': 'General Squaring', 'fa': 'مربع اعداد عمومی'},
        {'en': 'Duplex method.', 'fa': 'روش دوبلکس.'},
        'Squaring & Cubing', 'Vedic',
        {
            'en': 'To square any number: use the duplex (D). For a single digit a, D=a^2. For two digits ab, D=2ab.',
            'fa': 'برای مربع کردن هر عدد از روش دوبلکس (D) استفاده کنید.'
        },
        {'en': '23² = 529', 'fa': '۲۳² = ۵۲۹'},
        gen_vedic_squaring_general, steps_simple_mul
    ),
    Rule(
        'vedic-sqrt-perfect',
        {'en': 'Square Root (Perfect)', 'fa': 'جذر (کامل)'},
        {'en': 'Observation method.', 'fa': 'روش مشاهده.'},
        'Division & Roots', 'Vedic',
        {
            'en': 'Look at the last digit to find possible last digit of root. Find nearest square below.',
            'fa': 'به رقم آخر نگاه کنید تا رقم آخر ریشه را بیابید. نزدیک‌ترین مربع کمتر را پیدا کنید.'
        },
        {'en': 'sqrt(1225) = 35', 'fa': 'جذر ۱۲۲۵ = ۳۵'},
        gen_vedic_sqrt_perfect, steps_simple_mul
    ),
    Rule(
        'vedic-complementary-addition',
        {'en': 'Complementary Addition', 'fa': 'جمع متمم'},
        {'en': 'Completing the whole.', 'fa': 'تکمیل کردن کل.'},
        'Addition & Subtraction', 'Vedic',
        {
            'en': 'Look for numbers that add up to 10, 100, etc. to simplify addition.',
            'fa': 'به دنبال اعدادی بگردید که حاصل جمع آن‌ها ۱۰، ۱۰۰ و غیره می‌شود.'
        },
        {'en': '48 + 32 = 80', 'fa': '۴۸ + ۳۲ = ۸۰'},
        gen_vedic_complementary_addition, steps_simple_mul
    ),
    Rule(
        'vedic-subtraction-base',
        {'en': 'Subtraction from Base', 'fa': 'تفریق از مبنا'},
        {'en': 'All from 9 and the last from 10.', 'fa': 'همه از ۹ و آخرین از ۱۰.'},
        'Addition & Subtraction', 'Vedic',
        {
            'en': 'Subtract each digit from 9, and the last (non-zero) digit from 10.',
            'fa': 'هر رقم را از ۹ و آخرین رقم (غیر صفر) را از ۱۰ کم کنید.'
        },
        {'en': '1000 - 456 = 544', 'fa': '۱۰۰۰ - ۴۵۶ = ۵۴۴'},
        gen_vedic_subtraction_base, steps_vedic_sub_base
    ),
    Rule(
        'vedic-vertically-crosswise',
        {'en': 'Vertically and Crosswise', 'fa': 'عمودی و متقاطع'},
        {'en': 'Urdhva Tiryagbhyam Sutra.', 'fa': 'اوردوا تیریاگبیام سوترا.'},
        'Multiplication', 'Vedic',
        {
            'en': 'Multiply 2-digit numbers: Multiply units, cross-multiply and add, multiply tens.',
            'fa': 'ضرب اعداد ۲ رقمی: یکان‌ها را ضرب کنید، ضرب متقاطع و جمع، دهگان‌ها را ضرب کنید.'
        },
        {'en': '23 x 12 = 276', 'fa': '۲۳ × ۱۲ = ۲۷۶'},
        gen_vedic_vertically_crosswise, steps_simple_mul
    ),
    Rule(
        'vedic-square-near-base',
        {'en': 'Squaring near Base', 'fa': 'مربع نزدیک به مبنا'},
        {'en': 'Yavadunam Sutra.', 'fa': 'یاوادونام سوترا.'},
        'Squaring & Cubing', 'Vedic',
        {
            'en': 'To square near base: Left part = Number + Deficiency. Right part = Deficiency squared.',
            'fa': 'مربع نزدیک مبنا: بخش چپ = عدد + اختلاف. بخش راست = مجذور اختلاف.'
        },
        {'en': '13² = 169', 'fa': '۱۳² = ۱۶۹'},
        gen_vedic_square_near_base, steps_simple_mul
    ),
    Rule(
        'vedic-div-9',
        {'en': 'Division by 9', 'fa': 'تقسیم بر ۹'},
        {'en': 'Nikilam addition method.', 'fa': 'روش جمع نیکیلام.'},
        'Division & Roots', 'Vedic',
        {
            'en': 'Successively add digits for quotient and final remainder.',
            'fa': 'به طور متوالی ارقام را برای خارج‌قسمت و باقی‌مانده جمع کنید.'
        },
        {'en': '23 ÷ 9 = 2 R 5', 'fa': '۲۳ ÷ ۹ = ۲ باقی‌مانده ۵'},
        gen_vedic_div_9, steps_simple_mul
    ),
    Rule(
        'vedic-series-9',
        {'en': 'Multiplication by Series of 9s', 'fa': 'ضرب اعداد در سری ۹'},
        {'en': 'By one less than the previous one.', 'fa': 'با یکی کمتر از قبلی.'},
        'Multiplication', 'Vedic',
        {
            'en': 'Left part = number - 1. Right part = number from base (all from 9, last from 10).',
            'fa': 'بخش چپ = عدد منهای ۱. بخش راست = تفریق عدد از مبنا.'
        },
        {'en': '43 x 99 = 4257', 'fa': '۴۳ × ۹۹ = ۴۲۵۷'},
        gen_vedic_series_9, steps_vedic_series_9
    ),
    Rule(
        'vedic-ekadhikena',
        {'en': 'Units add to 10', 'fa': 'یکان‌های مکمل ۱۰'},
        {'en': 'Ekadhikena Purvena.', 'fa': 'اکادیکنا پورونا.'},
        'Multiplication', 'Vedic',
        {
            'en': 'Tens same and units sum 10: Tens*(Tens+1) | Units product.',
            'fa': 'دهگان یکسان و مجموع یکان‌ها ۱۰: دهگان در (دهگان+۱) | ضرب یکان‌ها.'
        },
        {'en': '42 x 48 = 2016', 'fa': '۴۲ × ۴۸ = ۲۰۱۶'},
        gen_vedic_ekadhikena, steps_vedic_ekadhikena
    ),
    Rule(
        'vedic-cubing',
        {'en': 'Cubing near Base', 'fa': 'مکعب نزدیک به مبنا'},
        {'en': 'Yavadunam (Cubing).', 'fa': 'یاوادونام (مکعب).'},
        'Squaring & Cubing', 'Vedic',
        {
            'en': 'To cube near base 10: Left: Num+2*Diff. Middle: 3*Diff^2. Right: Diff^3.',
            'fa': 'مکعب نزدیک مبنای ۱۰: چپ: عدد+۲×اختلاف. میانی: ۳×مجذور اختلاف. راست: مکعب اختلاف.'
        },
        {'en': '12³ = 1728', 'fa': '۱۲³ = ۱۷۲۸'},
        gen_vedic_cubing, steps_simple_mul
    )
]

rules_by_category = {}
for r in rules:
    if r.category not in rules_by_category:
        rules_by_category[r.category] = []
    rules_by_category[r.category].append(r)
