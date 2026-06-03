import random
import math

_PERSIAN_TRANS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
_POW10 = [10**i for i in range(10)]

def to_persian_digits(n):
    return str(n).translate(_PERSIAN_TRANS)

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
    return {"question": f"11 × {num}", "answer": 11 * num, "num": num}

def gen_tracht_12(**kwargs):
    num = random.randint(100, 9099)
    return {"question": f"12 × {num}", "answer": 12 * num, "num": num}

def gen_tracht_5(**kwargs):
    num = random.randint(100, 9099)
    return {"question": f"5 × {num}", "answer": 5 * num, "num": num}

def gen_tracht_6(**kwargs):
    num = random.randint(100, 9099)
    return {"question": f"6 × {num}", "answer": 6 * num, "num": num}

def gen_tracht_7(**kwargs):
    num = random.randint(100, 9099)
    return {"question": f"7 × {num}", "answer": 7 * num, "num": num}

def gen_tracht_8(**kwargs):
    num = random.randint(100, 9099)
    return {"question": f"8 × {num}", "answer": 8 * num, "num": num}

def gen_tracht_9(**kwargs):
    num = random.randint(100, 9099)
    return {"question": f"9 × {num}", "answer": 9 * num, "num": num}

def gen_tracht_4(**kwargs):
    num = random.randint(100, 9099)
    return {"question": f"4 × {num}", "answer": 4 * num, "num": num}

def gen_tracht_3(**kwargs):
    num = random.randint(100, 9099)
    return {"question": f"3 × {num}", "answer": 3 * num, "num": num}

def gen_tracht_13(**kwargs):
    num = random.randint(100, 9099)
    return {"question": f"13 × {num}", "answer": 13 * num, "num": num}

def gen_tracht_general(**kwargs):
    a = random.randint(11, 99)
    b = random.randint(11, 99)
    return {"question": f"{a} × {b}", "answer": a * b, "a": a, "b": b}

def gen_tracht_addition(num_operands=2, num_digits=3, **kwargs):
    operands = []
    for _ in range(num_operands):
        if num_digits == 0: # 0 means random
            d = random.randint(1, 6)
        else:
            d = num_digits
        operands.append(random.randint(_POW10[d-1], _POW10[d] - 1))
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
    base = 10 ** d
    num = random.randint(10**(d-1), base - 1)
    return {"question": f"{base} - {num}", "answer": base - num, "base": base, "num": num}

def gen_vedic_vertically_crosswise(**kwargs):
    a = random.randint(11, 99)
    b = random.randint(11, 99)
    return {"question": f"{a} × {b}", "answer": a * b, "a": a, "b": b}

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
    return {"question": f"{num} × 99", "answer": num * 99, "num": num}

def gen_vedic_ekadhikena(**kwargs):
    base = random.randint(1, 9) * 10
    d1 = random.randint(1, 9)
    d2 = 10 - d1
    a = base + d1
    b = base + d2
    return {"question": f"{a} × {b}", "answer": a * b, "a": a, "b": b}

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
        {'en': 'Multiplication by 11', 'fa': 'ضرب در ۱۱'},
        {'en': 'Add the neighbor rule.', 'fa': 'قانون اضافه کردن همسایه.'},
        'Multiplication', 'Trachtenberg',
        {
            'en': 'Trachtenberg rule for 11:\n1. The last digit of the number is the last digit of the answer.\n2. Each successive digit of the number is added to its neighbor on the right.\n3. The first digit of the number becomes the first digit of the answer (plus any carry).\nImagine a leading zero: 0432 x 11. 2+0=2, 3+2=5, 4+3=7, 0+4=4. Result: 4752.',
            'fa': 'قانون تراختنبرگ برای عدد ۱۱:\n۱. آخرین رقم عدد، همان آخرین رقم جواب است.\n۲. هر رقم عدد را با همسایه سمت راست آن جمع کنید.\n۳. اولین رقم عدد، اولین رقم جواب می‌شود (به اضافه هر عدد نقلی).\nیک صفر فرضی در ابتدا در نظر بگیرید: مثلاً ۱۱ × ۰۴۳۲. ۲+۰=۲، ۲+۳=۵، ۳+۴=۷، ۴+۰=۴. جواب: ۴۷۵۲.'
        },
        {'en': '11 × 432 = 4752', 'fa': '۱۱ × ۴۳۲ = ۴۷۵۲'},
        gen_tracht_11, steps_tracht_11
    ),
    Rule(
        'tracht-12',
        {'en': 'Multiplication by 12', 'fa': 'ضرب در ۱۲'},
        {'en': 'Double the digit and add neighbor.', 'fa': 'رقم را دو برابر کرده و با همسایه جمع کنید.'},
        'Multiplication', 'Trachtenberg',
        {
            'en': 'Trachtenberg rule for 12:\nDouble each digit and add its neighbor on the right.\n1. Last digit: Double it (neighbor is 0).\n2. Middle digits: Double the digit and add the digit to its right.\n3. Leading zero: Just add the digit that was previously to its right.\nExample: 12 × 413. (3*2)=6, (1*2)+3=5, (4*2)+1=9, (0*2)+4=4. Result: 4956.',
            'fa': 'قانون تراختنبرگ برای عدد ۱۲:\nهر رقم را دو برابر کرده و با همسایه سمت راست آن جمع کنید.\n۱. رقم آخر: آن را دو برابر کنید (همسایه ندارد یا همسایه‌اش ۰ است).\n۲. ارقام میانی: رقم را دو برابر کرده و با رقم سمت راستش جمع کنید.\n۳. صفر فرضی ابتدا: فقط رقمی را که قبلاً سمت راستش بود اضافه کنید.\nمثال: ۱۲ × ۴۱۳. (۳×۲)=۶، (۱×۲)+۳=۵، (۴×۲)+۱=۹، (۰×۲)+۴=۴. جواب: ۴۹۵۶.'
        },
        {'en': '12 × 413 = 4956', 'fa': '۱۲ × ۴۱۳ = ۴۹۵۶'},
        gen_tracht_12, lambda p, l: steps_tracht_mul(p, l, 12)
    ),
    Rule(
        'tracht-5',
        {'en': 'Multiplication by 5', 'fa': 'ضرب در ۵'},
        {'en': 'Half the neighbor rule.', 'fa': 'قانون نصف همسایه.'},
        'Multiplication', 'Trachtenberg',
        {
            'en': 'Trachtenberg rule for 5:\n1. For each digit, take half of its right-hand neighbor (ignore remainder).\n2. If the current digit is ODD, add 5 to that half.\nExample: 5 × 426. Neighbor of 6 is 0 (half is 0). 6 is even, so 0. Neighbor of 2 is 6 (half is 3). 2 is even, so 3. Neighbor of 4 is 2 (half is 1). 4 is even, so 1. Neighbor of leading 0 is 4 (half is 2). 0 is even, so 2. Result: 2130.',
            'fa': 'قانون تراختنبرگ برای عدد ۵:\n۱. برای هر رقم، نصف همسایه سمت راست آن را در نظر بگیرید (باقیمانده را نادیده بگیرید).\n۲. اگر خودِ رقم فرد است، ۵ واحد به آن نصف اضافه کنید.\nمثال: ۵ × ۴۲۶. همسایه ۶ صفر است (نصفش ۰). ۶ زوج است، پس ۰. همسایه ۲ عدد ۶ است (نصفش ۳). ۲ زوج است، پس ۳. همسایه ۴ عدد ۲ است (نصفش ۱). ۴ زوج است، پس ۱. همسایه صفرِ فرضی ۴ است (نصفش ۲). صفر زوج است، پس ۲. جواب: ۲۱۳۰.'
        },
        {'en': '5 × 426 = 2130', 'fa': '۵ × ۴۲۶ = ۲۱۳۰'},
        gen_tracht_5, lambda p, l: steps_tracht_mul(p, l, 5)
    ),
    Rule(
        'tracht-6',
        {'en': 'Multiplication by 6', 'fa': 'ضرب در ۶'},
        {'en': 'Add half the neighbor rule.', 'fa': 'قانون اضافه کردن نصف همسایه.'},
        'Multiplication', 'Trachtenberg',
        {
            'en': 'Trachtenberg rule for 6:\nTo each digit of the number, add half of its right-hand neighbor. If the current digit is ODD, add 5 to the result.\nExample: 6 × 422. (Imagining a leading zero: 0422)\n- 2 is even, neighbor 0: 2 + 0 = 2\n- 2 is even, neighbor 2: 2 + (2/2) = 3\n- 4 is even, neighbor 2: 4 + (2/2) = 5\n- 0 is even, neighbor 4: 0 + (4/2) = 2\nResult: 2532.',
            'fa': 'قانون تراختنبرگ برای عدد ۶:\nبه هر رقم، نصف همسایه سمت راست آن را اضافه کنید. اگر خودِ رقم فرد است، ۵ واحد به حاصل اضافه کنید.\nمثال: ۶ × ۴۲۲ (یک صفر فرضی در ابتدا در نظر بگیرید: ۰۴۲۲)\n- ۲ زوج است، همسایه ۰: ۲ + ۰ = ۲\n- ۲ زوج است، همسایه ۲: ۲ + (۲/۲) = ۳\n- ۴ زوج است، همسایه ۲: ۴ + (۲/۲) = ۵\n- ۰ زوج است، همسایه ۴: ۰ + (۴/۲) = ۲\nجواب: ۲۵۳۲.'
        },
        {'en': '6 × 422 = 2532', 'fa': '۶ × ۴۲۲ = ۲۵۳۲'},
        gen_tracht_6, steps_simple_mul
    ),
    Rule(
        'tracht-7',
        {'en': 'Multiplication by 7', 'fa': 'ضرب در ۷'},
        {'en': 'Double the digit and add half neighbor.', 'fa': 'رقم را دو برابر کرده و با نصف همسایه جمع کنید.'},
        'Multiplication', 'Trachtenberg',
        {
            'en': 'Trachtenberg rule for 7:\nDouble each digit and add half of its right-hand neighbor. If the current digit is ODD, add 5 to the result.\nExample: 7 × 242 (0242):\n- 2 is even, neighbor 0: (2*2) + 0 = 4\n- 4 is even, neighbor 2: (4*2) + (2/2) = 9\n- 2 is even, neighbor 4: (2*2) + (4/2) = 6\n- 0 is even, neighbor 2: (0*2) + (2/2) = 1\nResult: 1694.',
            'fa': 'قانون تراختنبرگ برای عدد ۷:\nهر رقم را دو برابر کرده و نصف همسایه سمت راستش را به آن اضافه کنید. اگر خودِ رقم فرد است، ۵ واحد به حاصل اضافه کنید.\nمثال: ۷ × ۲۴۲ (۰۲۴۲):\n- ۲ زوج است، همسایه ۰: (۲×۲) + ۰ = ۴\n- ۴ زوج است، همسایه ۲: (۴×۲) + ۱ = ۹\n- ۲ زوج است، همسایه ۴: (۲×۲) + ۲ = ۶\n- ۰ زوج است، همسایه ۲: (۰×۲) + ۱ = ۱\nجواب: ۱۶۹۴.'
        },
        {'en': '7 × 242 = 1694', 'fa': '۷ × ۲۴۲ = ۱۶۹۴'},
        gen_tracht_7, steps_simple_mul
    ),
    Rule(
        'tracht-8',
        {'en': 'Multiplication by 8', 'fa': 'ضرب در ۸'},
        {'en': 'Double the complement and add neighbor.', 'fa': 'دو برابر متمم و جمع با همسایه.'},
        'Multiplication', 'Trachtenberg',
        {
            'en': 'Trachtenberg rule for 8:\n1. Rightmost digit: Subtract from 10 and double the result.\n2. Middle digits: Subtract from 9, double the result, and add the neighbor on the right.\n3. Leftmost digit: Subtract 2 from the right-hand neighbor.\nExample: 8 × 432 (0432):\n- 2: (10-2)*2 = 16. Write 6, carry 1.\n- 3: (9-3)*2 + 2 + 1(carry) = 15. Write 5, carry 1.\n- 4: (9-4)*2 + 3 + 1(carry) = 14. Write 4, carry 1.\n- 0: (4-2) + 1(carry) = 3.\nResult: 3456.',
            'fa': 'قانون تراختنبرگ برای عدد ۸:\n۱. راست‌ترین رقم: از ۱۰ کم کرده و دو برابر کنید.\n۲. ارقام میانی: از ۹ کم کرده، دو برابر کنید و با همسایه سمت راست جمع کنید.\n۳. چپ‌ترین رقم (صفر فرضی): از همسایه سمت راستش ۲ واحد کم کنید.\nمثال: ۸ × ۴۳۲ (۰۴۳۲):\n- ۲: ۱۶ = ۲ × (۱۰-۲). ۶ را نوشته، ۱ را نگه دارید.\n- ۳: ۱۵ = ۱ + ۲ + ۲ × (۹-۳). ۵ را نوشته، ۱ را نگه دارید.\n- ۴: ۱۴ = ۱ + ۳ + ۲ × (۹-۴). ۴ را نوشته، ۱ را نگه دارید.\n- ۰: ۳ = ۱ + (۴-۲).\nجواب: ۳۴۵۶.'
        },
        {'en': '8 × 432 = 3456', 'fa': '۸ × ۴۳۲ = ۳۴۵۶'},
        gen_tracht_8, steps_simple_mul
    ),
    Rule(
        'tracht-9',
        {'en': 'Multiplication by 9', 'fa': 'ضرب در ۹'},
        {'en': 'Subtract from 10, then from 9.', 'fa': 'تفریق از ۱۰، سپس از ۹.'},
        'Multiplication', 'Trachtenberg',
        {
            'en': 'Trachtenberg rule for 9:\n1. Rightmost digit: Subtract from 10.\n2. Middle digits: Subtract from 9 and add the neighbor on the right.\n3. Leftmost digit: Subtract 1 from the right-hand neighbor.\nExample: 9 × 432 (0432):\n- 2: 10 - 2 = 8\n- 3: (9 - 3) + 2 = 8\n- 4: (9 - 4) + 3 = 8\n- 0: 4 - 1 = 3\nResult: 3888.',
            'fa': 'قانون تراختنبرگ برای عدد ۹:\n۱. راست‌ترین رقم: از ۱۰ کم کنید.\n۲. ارقام میانی: از ۹ کم کرده و با همسایه سمت راست جمع کنید.\n۳. چپ‌ترین رقم (صفر فرضی): از همسایه سمت راستش ۱ واحد کم کنید.\nمثال: ۹ × ۴۳۲ (۰۴۳۲):\n- ۲: ۸ = ۱۰ - ۲\n- ۳: ۸ = ۲ + (۹ - ۳)\n- ۴: ۸ = ۳ + (۹ - ۴)\n- ۰: ۳ = ۴ - ۱\nجواب: ۳۸۸۸.'
        },
        {'en': '9 × 432 = 3888', 'fa': '۹ × ۴۳۲ = ۳۸۸۸'},
        gen_tracht_9, steps_simple_mul
    ),
    Rule(
        'tracht-4',
        {'en': 'Multiplication by 4', 'fa': 'ضرب در ۴'},
        {'en': 'Subtract from 10/9 and add 5 if odd.', 'fa': 'تفریق از ۱۰/۹ و اضافه کردن ۵ در صورت فرد بودن.'},
        'Multiplication', 'Trachtenberg',
        {
            'en': 'Trachtenberg rule for 4:\n1. Rightmost digit: Subtract from 10. Add 5 if the digit is ODD.\n2. Middle digits: Subtract from 9, add half of the neighbor, and add 5 if the current digit is ODD.\n3. Leftmost digit: Take half of its right-hand neighbor and subtract 1.\nExample: 4 × 426 (0426):\n- 6: (10-6) = 4\n- 2: (9-2) + (6/2) = 10. Write 0, carry 1.\n- 4: (9-4) + (2/2) + 1(carry) = 7\n- 0: (4/2) - 1 = 1\nResult: 1704.',
            'fa': 'قانون تراختنبرگ برای عدد ۴:\n۱. راست‌ترین رقم: آن را از ۱۰ کم کنید. اگر رقم فرد است، ۵ واحد اضافه کنید.\n۲. ارقام میانی: رقم را از ۹ کم کنید، با نصف همسایه جمع کنید و اگر خود رقم فرد است، ۵ واحد اضافه کنید.\n۳. چپ‌ترین رقم (صفر فرضی): نصف همسایه سمت راست را منهای ۱ کنید.\nمثال: ۴ × ۴۲۶ (۰۴۲۶):\n- ۶: ۴ = ۱۰ - ۶\n- ۲: ۱۰ = ۳ + (۹ - ۲). ۰ را نوشته، ۱ را نگه دارید.\n- ۴: ۷ = ۱ + ۱ + (۹ - ۴)\n- ۰: ۱ = ۲ - ۱\nجواب: ۱۷۰۴.'
        },
        {'en': '4 × 426 = 1704', 'fa': '۴ × ۴۲۶ = ۱۷۰۴'},
        gen_tracht_4, steps_simple_mul
    ),
    Rule(
        'tracht-3',
        {'en': 'Multiplication by 3', 'fa': 'ضرب در ۳'},
        {'en': 'Double and subtract from 10/9.', 'fa': 'دو برابر کردن و تفریق از ۱۰/۹.'},
        'Multiplication', 'Trachtenberg',
        {
            'en': 'Trachtenberg rule for 3:\n1. Rightmost digit: Subtract from 10, double the result, and add 5 if the digit is ODD.\n2. Middle digits: Subtract from 9, double, add half of the neighbor, and add 5 if the current digit is ODD.\n3. Leftmost digit: Take half of its right-hand neighbor and subtract 2.\nExample: 3 × 432 (0432):\n- 2: (10-2)*2 = 16. Write 6, carry 1.\n- 3: (9-3)*2 + (2/2) + 5 + 1(carry) = 19. Write 9, carry 1.\n- 4: (9-4)*2 + (3/2) + 1(carry) = 12. Write 2, carry 1.\n- 0: (4/2) - 2 + 1(carry) = 1.\nResult: 1296.',
            'fa': 'قانون تراختنبرگ برای عدد ۳:\n۱. راست‌ترین رقم: از ۱۰ کم کرده، دو برابر کنید و اگر رقم فرد است، ۵ واحد اضافه کنید.\n۲. ارقام میانی: از ۹ کم کرده، دو برابر کنید، با نصف همسایه جمع کنید و اگر خود رقم فرد است، ۵ واحد اضافه کنید.\n۳. چپ‌ترین رقم (صفر فرضی): نصف همسایه سمت راست را منهای ۲ کنید.\nمثال: ۳ × ۴۳۲ (۰۴۳۲):\n- ۲: ۱۶ = ۲ × (۱۰-۲). ۶ را نوشته، ۱ را نگه دارید.\n- ۳: ۱۹ = ۱ + ۵ + ۱ + ۲ × (۹-۳). ۹ را نوشته، ۱ را نگه دارید.\n- ۴: ۱۲ = ۱ + ۱ + ۲ × (۹-۴). ۲ را نوشته، ۱ را نگه دارید.\n- ۰: ۱ = ۱ + ۲ - ۲\nجواب: ۱۲۹۶.'
        },
        {'en': '3 × 432 = 1296', 'fa': '۳ × ۴۳۲ = ۱۲۹۶'},
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
            'en': 'Vedic General Squaring (Duplex Method):\nTo square any number, we use the "Duplex" (D) for each part.\n- For 1 digit (a): D = a²\n- For 2 digits (ab): D = 2*a*b\n- For 3 digits (abc): D = 2*a*c + b²\nExample: 23². D(2)=4, D(23)=2*2*3=12, D(3)=9. Combine with carries: 4 | 12 | 9 = 529.',
            'fa': 'مربع عمومی (روش دوبلکس وِدیک):\nبرای مربع کردن هر عدد، از مقدار "دوبلکس" (D) برای هر بخش استفاده می‌کنیم.\n- برای ۱ رقم (a): D = a²\n- برای ۲ رقم (ab): D = ۲×a×b\n- برای ۳ رقم (abc): D = (۲×a×c) + b²\nمثال: ۲۳ به توان ۲. D(2)=۴، D(23)=۱۲، D(3)=۹. ترکیب با ارقام نقلی: ۹ | ۱۲ | ۴ که می‌شود ۵۲۹.'
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
            'en': 'Vedic Square Root (Perfect Squares):\n1. Look at the last digit to find two possible last digits for the root (e.g., if ends in 6, root ends in 4 or 6).\n2. Ignore the last two digits and find the largest square below the remaining part to find the first digit.\n3. Test which of the two possibilities is correct.\nExample: √1225. Ends in 5 -> root ends in 5. Below 12 is 3^2=9. So first digit is 3. Result: 35.',
            'fa': 'جذر اعداد کامل (روش وِدیک):\n۱. به رقم آخر نگاه کنید تا دو رقم احتمالی برای پایان ریشه پیدا کنید (مثلاً اگر به ۶ ختم شود، ریشه به ۴ یا ۶ ختم می‌شود).\n۲. دو رقم آخر را نادیده بگیرید و بزرگترین مربعی که از باقی‌مانده کوچکتر است را برای پیدا کردن رقم اول بیابید.\n۳. امتحان کنید کدام یک از دو حالت درست است.\nمثال: جذر ۱۲۲۵. به ۵ ختم می‌شود پس رقم آخر ۵ است. زیر ۱۲، مربعِ ۳ قرار دارد. پس رقم اول ۳ است. جواب: ۳۵.'
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
            'en': 'Vedic Complementary Addition:\nInstead of adding numbers directly, look for pairs that complete a multiple of 10 or 100. This "completing the whole" makes mental calculation much easier.\nExample: 48 + 32. 8 and 2 complete a 10. So (40+30) + (8+2) = 70 + 10 = 80.',
            'fa': 'جمع متمم (تکمیل کردن کل):\nبه جای جمع معمولی، به دنبال جفت‌اعدادی بگردید که حاصل‌جمع‌شان مضربی از ۱۰ یا ۱۰۰ می‌شود. این کار محاسبات ذهنی را بسیار ساده می‌کند.\nمثال: ۴۸ + ۳۲. اعداد ۸ و ۲ متمم هم هستند. پس ۸۰ = ۱۰ + ۷۰ = (۲+۸) + (۳۰+۴۰).'
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
            'en': 'Vedic Subtraction from Base:\nApply the "All from 9 and the Last from 10" rule.\n1. Subtract each digit from 9 starting from the left.\n2. Subtract the final non-zero digit from 10.\nExample: 1000 - 456. (9-4)=5, (9-5)=4, (10-6)=4. Result: 544.',
            'fa': 'تفریق از مبنا (همه از ۹ و آخرین از ۱۰):\n۱. تمام ارقام را از چپ به راست از ۹ کم کنید.\n۲. آخرین رقم (غیر صفر) را از ۱۰ کم کنید.\nمثال: ۴۵۶ - ۱۰۰۰. ۵ = ۴ - ۹. ۴ = ۵ - ۹. ۴ = ۶ - ۱۰. جواب: ۵۴۴.'
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
            'en': 'Vedic Vertically and Crosswise:\n1. Multiply units digits.\n2. Cross-multiply and add the results.\n3. Multiply tens digits.\nExample: 23 × 12. (3*2)=6, (2*2)+(3*1)=7, (2*1)=2. Result: 276.',
            'fa': 'عمودی و متقاطع (روش وِدیک):\n۱. یکان‌ها را در هم ضرب کنید.\n۲. به صورت ضربدری (متقاطع) ضرب کرده و نتایج را جمع کنید.\n۳. دهگان‌ها را در هم ضرب کنید.\nمثال: ۲۳ × ۱۲. یکان: ۶ = ۲×۳. دهگان: ۷ = (۱×۳) + (۲×۲). صدگان: ۲ = ۱×۲. جواب: ۲۷۶.'
        },
        {'en': '23 × 12 = 276', 'fa': '۲۳ × ۱۲ = ۲۷۶'},
        gen_vedic_vertically_crosswise, steps_simple_mul
    ),
    Rule(
        'vedic-square-near-base',
        {'en': 'Squaring near Base', 'fa': 'مربع نزدیک به مبنا'},
        {'en': 'Yavadunam Sutra.', 'fa': 'یاوادونام سوترا.'},
        'Squaring & Cubing', 'Vedic',
        {
            'en': 'Vedic Square near Base:\n1. Left part: Number + Deficiency (or - Excess).\n2. Right part: Square of the deficiency.\nExample: 13². Base 10, excess is 3. Left: 13+3=16. Right: 3^2=9. Result: 169.',
            'fa': 'مربع نزدیک به مبنا (روش وِدیک):\n۱. بخش چپ: عدد را با اختلافش از مبنا جمع کنید.\n۲. بخش راست: مجذور اختلاف را قرار دهید.\nمثال: ۱۳ به توان ۲. مبنا ۱۰ است و اختلاف ۳ واحد است. بخش چپ: ۱۶ = ۳ + ۱۳. بخش راست: ۹ = ۳ به توان ۲. جواب: ۱۶۹.'
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
            'en': 'Vedic Division by 9:\n1. First digit is first quotient digit.\n2. Add this to next digit for next quotient part.\n3. The final sum is the remainder.\nExample: 23 ÷ 9. First digit 2. Remainder: 2+3=5. Result: 2 R 5.',
            'fa': 'تقسیم بر ۹ (روش وِدیک):\n۱. اولین رقم، اولین رقمِ خارج‌قسمت است.\n۲. آن را با رقم بعدی جمع کنید تا رقم بعدی (یا باقی‌مانده) به دست آید.\n۳. جمع نهایی همان باقی‌مانده است.\nمثال: ۲۳ تقسیم بر ۹. رقم اول ۲ است. باقی‌مانده: ۵ = ۳ + ۲. جواب: ۲ با باقی‌مانده ۵.'
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
            'en': 'Vedic Multiplication by 9, 99, etc:\n1. Left part: Subtract 1 from the number.\n2. Right part: Use "All from 9 and last from 10" on the original number.\nExample: 43 × 99. Left: 43-1=42. Right: (9-4)=5, (10-3)=7. Result: 4257.',
            'fa': 'ضرب در ۹، ۹۹ و غیره (روش وِدیک):\n۱. بخش چپ: یک واحد از عدد کم کنید.\n۲. بخش راست: از قانون "همه از ۹ و آخرین از ۱۰" برای عدد اصلی استفاده کنید.\nمثال: ۴۳ × ۹۹. بخش چپ: ۴۲ = ۱ - ۴۳. بخش راست: ۵۷ (۳-۱۰ و ۴-۹). جواب: ۴۲۵۷.'
        },
        {'en': '43 × 99 = 4257', 'fa': '۴۳ × ۹۹ = ۴۲۵۷'},
        gen_vedic_series_9, steps_vedic_series_9
    ),
    Rule(
        'vedic-ekadhikena',
        {'en': 'Units add to 10', 'fa': 'یکان‌های مکمل ۱۰'},
        {'en': 'Ekadhikena Purvena.', 'fa': 'اکادیکنا پورونا.'},
        'Multiplication', 'Vedic',
        {
            'en': 'Vedic rule for same tens and units summing to 10:\n1. Left part: Multiply tens digit by its successor.\n2. Right part: Multiply the units digits.\nExample: 42 × 48. Left: 4*(4+1)=20. Right: 2*8=16. Result: 2016.',
            'fa': 'دهگان یکسان و مجموع یکان ۱۰ (روش وِدیک):\n۱. بخش چپ: دهگان را در عدد بعدی‌اش ضرب کنید.\n۲. بخش راست: یکان‌ها را در هم ضرب کنید.\nمثال: ۴۲ × ۴۸. بخش چپ: ۲۰ = (۱+۴) × ۴. بخش راست: ۱۶ = ۸ × ۲. جواب: ۲۰۱۶.'
        },
        {'en': '42 × 48 = 2016', 'fa': '۴۲ × ۴۸ = ۲۰۱۶'},
        gen_vedic_ekadhikena, steps_vedic_ekadhikena
    ),
    Rule(
        'vedic-cubing',
        {'en': 'Cubing near Base', 'fa': 'مکعب نزدیک به مبنا'},
        {'en': 'Yavadunam (Cubing).', 'fa': 'یاوادونام (مکعب).'},
        'Squaring & Cubing', 'Vedic',
        {
            'en': 'Vedic Cubing near Base 10:\n1. Left: Number + 2 * Deficiency.\n2. Middle: 3 * (Deficiency²).\n3. Right: Deficiency³.\nExample: 12³. Deficiency is 2. Left: 12+2*2=16. Middle: 3*(2^2)=12. Right: 2^3=8. Combine with carries: 16 | 12 | 8 = 1728.',
            'fa': 'مکعب نزدیک به مبنا (روش وِدیک):\n۱. بخش چپ: عدد + (۲ × اختلاف).\n۲. بخش میانی: ۳ × (مجذور اختلاف).\n۳. بخش راست: مکعب اختلاف.\nمثال: ۱۲ به توان ۳. اختلاف ۲ است. بخش چپ: ۱۶ = ۲×۲ + ۱۲. بخش میانی: ۱۲ = ۴ × ۳. بخش راست: ۸ = ۲ به توان ۳. ترکیب با ارقام نقلی: ۸ | ۱۲ | ۱۶ که می‌شود ۱۷۲۸.'
        },
        {'en': '12³ = 1728', 'fa': '۱۲³ = ۱۷۲۸'},
        gen_vedic_cubing, steps_simple_mul
    )
]

rules_by_category = {}
rules_by_method = {}
rules_by_system_category = {} # Optimized for UI navigation
for r in rules:
    if r.category not in rules_by_category:
        rules_by_category[r.category] = []
    rules_by_category[r.category].append(r)

    if r.method not in rules_by_method:
        rules_by_method[r.method] = []
    rules_by_method[r.method].append(r)

    sys_cat_key = (r.method, r.category)
    if sys_cat_key not in rules_by_system_category:
        rules_by_system_category[sys_cat_key] = []
    rules_by_system_category[sys_cat_key].append(r)
