import random
import math

def to_persian_digits(n):
    n = str(n)
    english_digits = "0123456789"
    persian_digits = "۰۱۲۳۴۵۶۷۸۹"
    translation_table = str.maketrans(english_digits, persian_digits)
    return n.translate(translation_table)

class Rule:
    def __init__(self, id, name, description, method, explanation, example, generate_problem_fn):
        self.id = id
        self.name = name
        self.description = description
        self.method = method
        self.explanation = explanation
        self.example = example
        self.generate_problem_fn = generate_problem_fn

    def generate_problem(self, **kwargs):
        return self.generate_problem_fn(**kwargs)

def gen_tracht_11(**kwargs):
    num = random.randint(100, 9099)
    return {"question": to_persian_digits(f"11 × {num}"), "answer": 11 * num}

def gen_tracht_12(**kwargs):
    num = random.randint(100, 9099)
    return {"question": to_persian_digits(f"12 × {num}"), "answer": 12 * num}

def gen_tracht_5(**kwargs):
    num = random.randint(100, 9099)
    return {"question": to_persian_digits(f"5 × {num}"), "answer": 5 * num}

def gen_vedic_square_5(**kwargs):
    base = random.randint(1, 12)
    num = base * 10 + 5
    return {"question": to_persian_digits(f"{num}²"), "answer": num * num}

def gen_vedic_base_10(**kwargs):
    a = random.randint(7, 13)
    b = random.randint(7, 13)
    return {"question": to_persian_digits(f"{a} × {b}"), "answer": a * b}

def gen_vedic_base_100(**kwargs):
    a = random.randint(90, 110)
    b = random.randint(90, 110)
    return {"question": to_persian_digits(f"{a} × {b}"), "answer": a * b}

def gen_vedic_squaring_general(**kwargs):
    num = random.randint(11, 99)
    return {"question": to_persian_digits(f"{num}²"), "answer": num * num}

def gen_vedic_sqrt_perfect(**kwargs):
    root = random.randint(10, 99)
    num = root * root
    return {"question": to_persian_digits(f"√{num}"), "answer": root}

def gen_tracht_addition(num_operands=2, num_digits=3, **kwargs):
    operands = []
    for _ in range(num_operands):
        if num_digits == 0: # 0 means random
            d = random.randint(1, 6)
        else:
            d = num_digits
        operands.append(random.randint(10**(d-1), 10**d - 1))

    question = " + ".join(map(str, operands))
    answer = sum(operands)
    return {"question": to_persian_digits(question), "answer": answer}

def gen_tracht_6(**kwargs):
    num = random.randint(100, 9099)
    return {"question": to_persian_digits(f"6 × {num}"), "answer": 6 * num}

def gen_tracht_7(**kwargs):
    num = random.randint(100, 9099)
    return {"question": to_persian_digits(f"7 × {num}"), "answer": 7 * num}

def gen_tracht_8(**kwargs):
    num = random.randint(100, 9099)
    return {"question": to_persian_digits(f"8 × {num}"), "answer": 8 * num}

def gen_tracht_9(**kwargs):
    num = random.randint(100, 9099)
    return {"question": to_persian_digits(f"9 × {num}"), "answer": 9 * num}

def gen_tracht_4(**kwargs):
    num = random.randint(100, 9099)
    return {"question": to_persian_digits(f"4 × {num}"), "answer": 4 * num}

def gen_tracht_3(**kwargs):
    num = random.randint(100, 9099)
    return {"question": to_persian_digits(f"3 × {num}"), "answer": 3 * num}

def gen_vedic_base_1000(**kwargs):
    a = random.randint(990, 1010)
    b = random.randint(990, 1010)
    return {"question": to_persian_digits(f"{a} × {b}"), "answer": a * b}

def gen_vedic_complementary_addition(num_operands=2, num_digits=3, **kwargs):
    if num_operands > 2 or num_digits != 3:
        return gen_tracht_addition(num_operands=num_operands, num_digits=num_digits)

    base = random.randint(1, 8) * 10
    diff = random.randint(1, 9)
    a = base + diff
    b = (10 - diff) + random.randint(0, 4) * 10
    return {"question": to_persian_digits(f"{a} + {b}"), "answer": a + b}

def gen_vedic_subtraction_base(num_digits=3, **kwargs):
    if num_digits == 0:
        d = random.randint(1, 6)
    else:
        d = num_digits
    base = 10 ** d
    num = random.randint(10**(d-1), base - 1)
    return {"question": to_persian_digits(f"{base} - {num}"), "answer": base - num}

def gen_vedic_vertically_crosswise(**kwargs):
    a = random.randint(11, 99)
    b = random.randint(11, 99)
    return {"question": to_persian_digits(f"{a} × {b}"), "answer": a * b}

def gen_vedic_square_near_base(**kwargs):
    base = 10 ** random.randint(1, 2)
    diff = random.randint(-5, 5)
    if diff == 0: diff = 1
    num = base + diff
    return {"question": to_persian_digits(f"{num}²"), "answer": num * num}

def gen_tracht_13(**kwargs):
    num = random.randint(100, 9099)
    return {"question": to_persian_digits(f"13 × {num}"), "answer": 13 * num}

def gen_tracht_general(**kwargs):
    a = random.randint(11, 99)
    b = random.randint(11, 99)
    return {"question": to_persian_digits(f"{a} × {b}"), "answer": a * b}

def gen_tracht_division(**kwargs):
    divisor = random.randint(2, 12)
    quotient = random.randint(10, 99)
    num = divisor * quotient
    return {"question": to_persian_digits(f"{num} ÷ {divisor}"), "answer": quotient}

def gen_tracht_sqrt(**kwargs):
    root = random.randint(10, 40)
    num = root * root
    return {"question": to_persian_digits(f"√{num}"), "answer": root}

def gen_vedic_div_9(**kwargs):
    num = random.randint(10, 89)
    return {"question": to_persian_digits(f"{num} ÷ 9"), "answer": num // 9}

def gen_vedic_series_9(**kwargs):
    num = random.randint(11, 99)
    return {"question": to_persian_digits(f"{num} × 99"), "answer": num * 99}

def gen_vedic_ekadhikena(**kwargs):
    base = random.randint(1, 9) * 10
    d1 = random.randint(1, 9)
    d2 = 10 - d1
    a = base + d1
    b = base + d2
    return {"question": to_persian_digits(f"{a} × {b}"), "answer": a * b}

def gen_vedic_cubing(**kwargs):
    base = 10
    diff = random.randint(1, 3)
    num = base + diff
    return {"question": to_persian_digits(f"{num}³"), "answer": num ** 3}

rules = [
    Rule(
        'tracht-11', 'ضرب اعداد در ۱۱', 'قانون اضافه کردن همسایه.', 'تراختنبرگ',
        'برای ضرب یک عدد در ۱۱: ۱. آخرین رقم عدد، آخرین رقم جواب است. ۲. هر رقم متوالی عدد با همسایه سمت راست خود جمع می‌شود. ۳. اولین رقم عدد (به اضافه هر رقم نقلی) اولین رقم جواب می‌شود.\n\nبررسی: مجموع ارقام(۱۱) × مجموع ارقام(عدد) = مجموع ارقام(جواب).',
        '۱۱ × ۴۳۲ = ۴ (۴+۳) (۳+۲) ۲ = ۴۷۵۲', gen_tracht_11
    ),
    Rule(
        'tracht-12', 'ضرب اعداد در ۱۲', 'رقم را دو برابر کرده و با همسایه جمع کنید.', 'تراختنبرگ',
        'برای ضرب در ۱۲: هر رقم را به ترتیب دو برابر کرده و با همسایه خود جمع کنید.\n\nبررسی: مجموع ارقام(۱۲) × مجموع ارقام(عدد) = مجموع ارقام(جواب).',
        '۱۲ × ۴۱۳ = (۲×۴+۱) (۲×۱+۳) (۲×۳) = ۴۹۵۶', gen_tracht_12
    ),
    Rule(
        'tracht-5', 'ضرب اعداد در ۵', 'قانون نصف همسایه.', 'تراختنبرگ',
        'از نصف همسایه استفاده کنید: اگر رقم فرد است، ۵ را به نصف همسایه اضافه کنید.\n\nبررسی: مجموع ارقام(۵) × مجموع ارقام(عدد) = مجموع ارقام(جواب).',
        '۵ × ۴۲۶ = (نصف ۴) (نصف ۲) (نصف ۶) ۰ = ۲۱۳۰', gen_tracht_5
    ),
    Rule(
        'vedic-square-5', 'مربع اعداد مختوم به ۵', 'با یکی بیشتر از قبلی.', 'ودایی',
        'برای محاسبه مربع عددی که به ۵ ختم می‌شود: قسمت قبل از ۵ را در (خودش + ۱) ضرب کنید، سپس ۲۵ را به انتهای آن اضافه کنید.\n\nبررسی: مجموع ارقام(عدد)² = مجموع ارقام(جواب).',
        '۳۵² = (۳ × ۴) | ۲۵ = ۱۲۲۵', gen_vedic_square_5
    ),
    Rule(
        'vedic-base-10', 'ضرب نزدیک به مبنای ۱۰', 'همه از ۹ و آخرین از ۱۰.', 'ودایی',
        'اعداد نزدیک به ۱۰ را ضرب کنید. کمبودها را پیدا کنید، آن‌ها را برای قسمت راست ضرب کنید، و برای قسمت چپ به صورت متقاطع جمع کنید.\n\nبررسی: روش طرد ۹.',
        '۹ × ۸: اختلاف‌ها ۱ و ۲ هستند. ۱×۲=۲. ۹-۲=۷ یا ۸-۱=۷. جواب ۷۲.', gen_vedic_base_10
    ),
    Rule(
        'vedic-base-100', 'ضرب نزدیک به مبنای ۱۰۰', 'نیکیلام سوترا.', 'ودایی',
        'اعداد نزدیک به ۱۰۰ را ضرب کنید. کمبودها را پیدا کنید، آن‌ها را برای قسمت راست (۲ رقم) ضرب کنید، و برای قسمت چپ به صورت متقاطع جمع کنید.\n\nبررسی: روش طرد ۹.',
        '۹۷ × ۹۶: اختلاف‌ها ۳ و ۴. ۳×۴=۱۲. ۹۷-۴=۹۳. جواب ۹۳۱۲.', gen_vedic_base_100
    ),
    Rule(
        'vedic-squaring-general', 'مربع اعداد عمومی', 'روش دوبلکس.', 'ودایی',
        'برای مربع کردن هر عدد: از دوبلکس (D) استفاده کنید. برای یک رقم a، D=a^۲. برای دو رقم ab، D=۲ab.\n\nبررسی: مجموع ارقام(عدد)² = مجموع ارقام(جواب).',
        '۲۳² = D(۲) | D(۲۳) | D(۳) = ۴ | ۱۲ | ۹ = ۵۲۹', gen_vedic_squaring_general
    ),
    Rule(
        'vedic-sqrt-perfect', 'جذر (کامل)', 'روش مشاهده.', 'ودایی',
        'به رقم آخر نگاه کنید تا رقم آخر احتمالی ریشه را پیدا کنید. دو رقم آخر را نادیده بگیرید و نزدیک‌ترین مربع کمتر از عدد باقی‌مانده را پیدا کنید.\n\nبررسی: مربع نتیجه باید برابر با عدد اصلی باشد.',
        'جذر ۱۲۲۵: به ۵ ختم می‌شود، پس ریشه به ۵ ختم می‌شود. ۱۲ بین ۳^۲ و ۴^۲ است. پس رقم دهگان ۳ است. جواب ۳۵.', gen_vedic_sqrt_perfect
    ),
    Rule(
        'tracht-addition', 'جمع سریع', 'روش ستونی چپ به راست.', 'تراختنبرگ',
        'ستون‌ها را از چپ به راست جمع کنید، سپس رقم‌های نقلی را تنظیم کنید.\n\nبررسی: مجموع ارقام هر عدد = مجموع ارقام کل.',
        '۴۵۶ + ۱۲۳ = (۴+۱) (۵+۲) (۶+۳) = ۵۷۹', gen_tracht_addition
    ),
    Rule(
        'tracht-6', 'ضرب اعداد در ۶', 'قانون اضافه کردن نصف همسایه.', 'تراختنبرگ',
        'برای ضرب در ۶: نصف همسایه را به هر رقم اضافه کنید. اگر رقم فرد است، ۵ را اضافه کنید.\n\nبررسی: مجموع ارقام(۶) × مجموع ارقام(عدد) = مجموع ارقام(جواب).',
        '۶ × ۴۲۲ = (۴+۱) (۲+۱) (۲+۰) = ۲۵۳۲', gen_tracht_6
    ),
    Rule(
        'tracht-7', 'ضرب اعداد در ۷', 'رقم را دو برابر کرده و با نصف همسایه جمع کنید.', 'تراختنبرگ',
        'برای ضرب در ۷: هر رقم را دو برابر کرده و با نصف همسایه جمع کنید. اگر رقم فرد است، ۵ را اضافه کنید.\n\nبررسی: مجموع ارقام(۷) × مجموع ارقام(عدد) = مجموع ارقام(جواب).',
        '۷ × ۲۴۲ = (۲×۲+۲) (۲×۴+۱) (۲×۲+۰) = ۱۶۹۴', gen_tracht_7
    ),
    Rule(
        'tracht-8', 'ضرب اعداد در ۸', 'دو برابر متمم و جمع با همسایه.', 'تراختنبرگ',
        'برای ضرب در ۸: ۱. سمت راست‌ترین: ۲ × (۱۰ - رقم). ۲. میانی: (۲ × (۹ - رقم)) + همسایه. ۳. سمت چپ‌ترین: همسایه - ۲.\n\nبررسی: مجموع ارقام(۸) × مجموع ارقام(عدد) = مجموع ارقام(جواب).',
        '۸ × ۴۳۲: (۱۰-۲)×۲=۱۶; (۹-۳)×۲+۲+۱=۱۵ (۱ منتقل میشه); (۹-۴)×۲+۳+۱=۱۴ (۱ منتقل میشه); ۴-۲+۱=۳. جواب: ۳۴۵۶', gen_tracht_8
    ),
    Rule(
        'tracht-9', 'ضرب اعداد در ۹', 'تفریق از ۱۰، سپس از ۹.', 'تراختنبرگ',
        'برای ضرب در ۹: ۱. سمت راست‌ترین رقم را از ۱۰ کم کنید. ۲. برای سایر ارقام، آن‌ها را از ۹ کم کرده و با همسایه جمع کنید. ۳. برای صفر پیشرو، ۱ را از همسایه کم کنید.\n\nبررسی: مجموع ارقام نتیجه باید ۹ باشد.',
        '۹ × ۴۳۲: (۱۰-۲=۸), (۹-۳+۲=۸), (۹-۴+۳=۸), (۴-۱=۳) = ۳۸۸۸', gen_tracht_9
    ),
    Rule(
        'vedic-base-1000', 'ضرب نزدیک به مبنای ۱۰۰۰', 'نیکیلام سوترا (مبنای ۱۰۰۰).', 'ودایی',
        'اعداد نزدیک به ۱۰۰۰ را ضرب کنید. کمبودها را پیدا کنید، آن‌ها را برای قسمت راست (۳ رقم) ضرب کنید، و برای قسمت چپ به صورت متقاطع جمع کنید.\n\nبررسی: روش طرد ۹.',
        '۹۹۸ × ۹۹۷: اختلاف‌ها ۲ و ۳. ۲×۳=۰۰۶. ۹۹۸-۳=۹۹۵. جواب ۹۹۵۰۰۶.', gen_vedic_base_1000
    ),
    Rule(
        'vedic-complementary-addition', 'جمع متمم', 'تکمیل کردن کل.', 'ودایی',
        'به دنبال اعدادی بگردید که حاصل جمع آن‌ها ۱۰، ۱۰۰ و غیره می‌شود تا جمع ساده‌تر شود.\n\nبررسی: مجموع مجموع ارقام = مجموع ارقام کل.',
        '۴۸ + ۳۲ = ۴۰ + ۳۰ + (۸ + ۲) = ۷۰ + ۱۰ = ۸۰', gen_vedic_complementary_addition
    ),
    Rule(
        'tracht-4', 'ضرب اعداد در ۴', 'تفریق از ۹ و جمع با نصف همسایه.', 'تراختنبرگ',
        'برای ضرب در ۴: ۱. رقم سمت راست را از ۱۰ کم کنید، اگر رقم فرد است ۵ را اضافه کنید. ۲. برای سایر ارقام، از ۹ کم کنید، نصف همسایه را اضافه کنید و اگر رقم فرد است ۵ را اضافه کنید. ۳. صفر پیشرو: نصف همسایه منهای ۱.\n\nبررسی: مجموع ارقام(۴) × مجموع ارقام(عدد) = مجموع ارقام(جواب).',
        '۴ × ۴۲۶: (۱۰-۶=۴), (۹-۲+۳=۱۰, ۱ منتقل میشه), (۹-۴+۱+۱=۷), (۲-۱=۱). جواب ۱۷۰۴', gen_tracht_4
    ),
    Rule(
        'tracht-3', 'ضرب اعداد در ۳', 'دو برابر متمم و جمع با نصف همسایه.', 'تراختنبرگ',
        'برای ضرب در ۳: ۱. سمت راست‌ترین: از ۱۰ کم کنید، دو برابر کنید، اگر فرد است ۵ را اضافه کنید. ۲. میانی: از ۹ کم کنید، دو برابر کنید، نصف همسایه را اضافه کنید، اگر فرد است ۵ را اضافه کنید. ۳. سمت چپ‌ترین: نصف همسایه منهای ۲.\n\nبررسی: مجموع ارقام(۳) × مجموع ارقام(عدد) = مجموع ارقام(جواب).',
        '۳ × ۴۲۲: (۱۰-۲)×۲=۱۶; (۹-۲)×۲+۱+۱=۱۶; (۹-۴)×۲+۱+۱=۱۲; ۲-۲+۱=۱. جواب: ۱۲۶۶', gen_tracht_3
    ),
    Rule(
        'vedic-subtraction-base', 'تفریق از مبنا', 'همه از ۹ و آخرین از ۱۰.', 'ودایی',
        'برای تفریق یک عدد از توان ۱۰: هر رقم را از ۹ و آخرین رقم (غیر صفر) را از ۱۰ کم کنید.\n\nبررسی: پاسخ + عدد = مبنا.',
        '۱۰۰۰ - ۴۵۶ = (۹-۴) (۹-۵) (۱۰-۶) = ۵۴۴', gen_vedic_subtraction_base
    ),
    Rule(
        'vedic-vertically-crosswise', 'عمودی و متقاطع', 'اوردوا تیریاگبیام سوترا.', 'ودایی',
        'ضرب اعداد ۲ رقمی: ۱. یکان‌ها را ضرب کنید (ستون راست). ۲. ضرب متقاطع کرده و جمع کنید. ۳. دهگان‌ها را ضرب کنید (ستون چپ). در صورت نیاز رقم نقلی را منتقل کنید.\n\nبررسی: روش طرد ۹.',
        '۲۳ × ۱۲: (۲×۱) | (۲×۲ + ۳×۱) | (۳×۲) = ۲ | ۷ | ۶ = ۲۷۶', gen_vedic_vertically_crosswise
    ),
    Rule(
        'vedic-square-near-base', 'مربع نزدیک به مبنا', 'یاوادونام سوترا.', 'ودایی',
        'برای مربع کردن عددی نزدیک به مبنا (۱۰، ۱۰۰): ۱. قسمت چپ: عدد + اختلاف. ۲. قسمت راست: مجذور اختلاف.\n\nبررسی: مجموع ارقام(عدد)² = مجموع ارقام(جواب).',
        '۱۳²: مبنا ۱۰، اختلاف +۳. (۱۳+۳) | (۳²) = ۱۶ | ۹ = ۱۶۹', gen_vedic_square_near_base
    ),
    Rule(
        'tracht-13', 'ضرب اعداد در ۱۳', 'رقم را سه برابر کرده و با همسایه جمع کنید.', 'تراختنبرگ',
        'برای ضرب در ۱۳: هر رقم را به ترتیب سه برابر کرده و با همسایه خود جمع کنید.\n\nبررسی: روش طرد ۹. مجموع ارقام حاصل‌ضرب باید برابر با مجموع ارقام (۱ + ۳) ضرب در مجموع ارقام عدد باشد.',
        '۱۳ × ۱۲ = (۳×۰+۱) (۳×۱+۲) (۳×۲) = ۱۵۶.', gen_tracht_13
    ),
    Rule(
        'tracht-general', 'ضرب عمومی', 'روش دو انگشتی.', 'تراختنبرگ',
        'ضرب مستقیم بدون جدول. از قانون "بیرون-درون" استفاده کنید: جفت بیرونی و جفت درونی را ضرب کرده و جمع کنید. برای هر موقعیت تکرار کنید.\n\nبررسی: روش طرد ۹.',
        '۲۳ × ۱۲ = (۲×۱) | (۲×۲ + ۳×۱) | (۳×۲) = ۲۷۶', gen_tracht_general
    ),
    Rule(
        'tracht-division', 'تقسیم مستقیم', 'روش سرعت و دقت.', 'تراختنبرگ',
        'با استفاده از رقم پیشرو مقسوم‌علیه تقسیم کنید، سپس نتایج حاصل‌ضرب‌های بعدی را از باقی‌مانده کم کنید.\n\nبررسی: حاصل‌ضرب نتیجه در مقسوم‌علیه باید برابر با عدد اصلی باشد.',
        '۱۵۶ ÷ ۱۲ = ۱۳', gen_tracht_division
    ),
    Rule(
        'tracht-sqrt', 'جذر', 'استخراج سیستماتیک.', 'تراختنبرگ',
        'ارقام را با استفاده از روش سیستماتیک "محاسبه معکوس" بر اساس نزدیک‌ترین مربع و باقی‌مانده‌ها استخراج کنید.\n\nبررسی: مربع نتیجه باید برابر با عدد اصلی باشد.',
        'جذر ۶۲۵ = ۲۵', gen_tracht_sqrt
    ),
    Rule(
        'vedic-div-9', 'تقسیم بر ۹', 'روش جمع نیکیلام.', 'ودایی',
        'رقم اول همان رقم اول خارج‌قسمت است. به طور متوالی ارقام را برای ارقام بعدی خارج‌قسمت و باقی‌مانده نهایی جمع کنید.\n\nبررسی: خارج‌قسمت × ۹ + باقی‌مانده = عدد اصلی.',
        '۲۳ ÷ ۹ = ۲ باقی‌مانده ۵', gen_vedic_div_9
    ),
    Rule(
        'vedic-series-9', 'ضرب اعداد در سری ۹', 'با یکی کمتر از قبلی.', 'ودایی',
        'برای بخش چپ ۱ واحد از عدد کم کنید، سپس برای بخش راست عدد را از مبنا کم کنید (همه از ۹، آخرین از ۱۰).\n\nبررسی: روش طرد ۹.',
        '۴۳ × ۹۹ = (۴۳-۱) | (۱۰۰-۴۳) = ۴۲۵۷', gen_vedic_series_9
    ),
    Rule(
        'vedic-ekadhikena', 'یکان‌های مکمل ۱۰', 'اکادیکنا پورونا.', 'ودایی',
        'اگر ارقام دهگان یکسان و مجموع یکان‌ها ۱۰ باشد: دهگان را در (دهگان + ۱) برای بخش چپ ضرب کنید، و یکان‌ها را برای بخش راست در هم ضرب کنید.\n\nبررسی: روش طرد ۹.',
        '۴۲ × ۴۸ = (۴×۵) | (۲×۸) = ۲۰۱۶', gen_vedic_ekadhikena
    ),
    Rule(
        'vedic-cubing', 'مکعب نزدیک به مبنا', 'یاوادونام (مکعب).', 'ودایی',
        'برای محاسبه مکعب عددی نزدیک به مبنای ۱۰: ۱. چپ: عدد + ۲ × اختلاف. ۲. میانی: ۳ × مجذور اختلاف. ۳. راست: مکعب اختلاف.\n\nبررسی: مجموع ارقام(عدد)³ = مجموع ارقام(جواب).',
        '۱۲³: مبنا ۱۰، اختلاف ۲. (۱۲+۴) | (۳×۴) | (۸) = ۱۶ | ۱۲ | ۸ = ۱۷۲۸', gen_vedic_cubing
    )
]

rules_by_method = {
    "تراختنبرگ": [r for r in rules if r.method == "تراختنبرگ"],
    "ودایی": [r for r in rules if r.method == "ودایی"]
}
