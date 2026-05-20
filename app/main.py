import flet as ft
import time
import asyncio
import sys
import os

# Add the current directory to sys.path to ensure local modules are found
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

try:
    from math_logic import rules, rules_by_category, to_lang_digits
except ImportError:
    from app.math_logic import rules, rules_by_category, to_lang_digits

# Theme Colors
COLOR_PRIMARY = "#00D4C8"  # Vibrant Teal
COLOR_ACCENT = "#FF6B00"   # Bright Orange
COLOR_BG = "#0F172A"       # Deep Black / Dark Navy
COLOR_SURFACE = "#1E2937"  # Darker Surface
COLOR_SUCCESS = "#00FF7F"  # Spring Green

LOCALIZED_UI = {
    'en': {
        'title': 'MathBeast',
        'subtitle': 'Master Rapid Calculation',
        'back_categories': 'Back to Categories',
        'back_methods': 'Back to methods',
        'learn': 'Learn',
        'practice': 'Practice',
        'learn_desc': 'Study the theory and see examples.',
        'practice_desc': 'Test your speed and accuracy.',
        'target': 'Target:',
        'score': 'Score:',
        'streak': 'Streak:',
        'time': 'Time:',
        'check': 'Check Answer',
        'next': 'Next Problem',
        'correct': 'Correct!',
        'wrong': 'Wrong. The answer was',
        'enter_answer': 'Enter answer',
        'theory_title': 'Theory & Shortcuts',
        'example_title': 'Example',
        'steps_title': 'Step-by-Step Guide',
        'custom_panel': 'Customization Panel',
        'apply_restart': 'Apply & Restart',
        'count': 'Count',
        'digits': 'Digits per number',
        'random': 'Random',
        'footer': '© 2024 MathBeast. Built with Flet.'
    },
    'fa': {
        'title': 'MathBeast',
        'subtitle': 'تسلط بر محاسبات ذهنی سریع',
        'back_categories': 'بازگشت به دسته‌بندی‌ها',
        'back_methods': 'بازگشت به روش‌ها',
        'learn': 'آموزش',
        'practice': 'تمرین',
        'learn_desc': 'مطالعه تئوری و مشاهده مثال‌ها.',
        'practice_desc': 'تست سرعت و دقت شما.',
        'target': 'هدف:',
        'score': 'امتیاز:',
        'streak': 'توالی:',
        'time': 'زمان:',
        'check': 'بررسی پاسخ',
        'next': 'مسئله بعدی',
        'correct': 'آفرین! درست بود.',
        'wrong': 'اشتباه بود. جواب صحیح:',
        'enter_answer': 'پاسخ را وارد کنید',
        'theory_title': 'تئوری و میان‌برها',
        'example_title': 'مثال',
        'steps_title': 'راهنمای مرحله‌به‌مرحله',
        'custom_panel': 'پنل تنظیمات',
        'apply_restart': 'اعمال و شروع مجدد',
        'count': 'تعداد',
        'digits': 'ارقام هر عدد',
        'random': 'تصادفی',
        'footer': '© ۲۰۲۴ MathBeast. ساخته شده با Flet.'
    }
}

CATEGORIES_INFO = {
    'Multiplication': {
        'en': 'Multiplication',
        'fa': 'ضرب',
        'desc_en': 'Techniques for rapid multiplication.',
        'desc_fa': 'تکنیک‌های ضرب سریع اعداد.',
        'icon': ft.Icons.GRID_VIEW,
        'color': COLOR_PRIMARY
    },
    'Addition & Subtraction': {
        'en': 'Addition & Subtraction',
        'fa': 'جمع و تفریق',
        'desc_en': 'Speed up your basic arithmetic.',
        'desc_fa': 'سرعت بخشیدن به عملیات پایه.',
        'icon': ft.Icons.ADD_CIRCLE_OUTLINE,
        'color': ft.Colors.BLUE_400
    },
    'Squaring & Cubing': {
        'en': 'Squaring & Cubing',
        'fa': 'مربع و مکعب',
        'desc_en': 'Calculate powers in seconds.',
        'desc_fa': 'محاسبه توان‌ها در چند ثانیه.',
        'icon': ft.Icons.EXPOSURE_PLUS_2,
        'color': COLOR_ACCENT
    },
    'Division & Roots': {
        'en': 'Division & Roots',
        'fa': 'تقسیم و جذر',
        'desc_en': 'Master division and square roots.',
        'desc_fa': 'تسلط بر تقسیم و ریشه‌های دوم.',
        'icon': ft.Icons.FUNCTIONS,
        'color': ft.Colors.PURPLE_400
    }
}

class FastMathApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.lang = 'fa'
        self.update_page_config()

        self.selected_rule = None
        self.current_problem = None
        self.score = 0
        self.total = 0
        self.streak = 0
        self.start_time = None
        self.timer_running = False
        self.timer_id = 0
        self.mode = "Learn"

        self.setup_ui()

    def update_page_config(self):
        self.page.title = LOCALIZED_UI[self.lang]['title']
        self.page.rtl = (self.lang == 'fa')
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.padding = 20
        self.page.bgcolor = COLOR_BG
        self.page.scroll = ft.ScrollMode.AUTO

    def toggle_language(self, e):
        self.lang = 'en' if self.lang == 'fa' else 'fa'
        self.update_page_config()
        # Full UI refresh
        self.page.controls.clear()
        self.setup_ui()

    def setup_ui(self):
        ui = LOCALIZED_UI[self.lang]

        lang_btn = ft.Container(
            content=ft.Text("en" if self.lang == 'fa' else "فا", weight=ft.FontWeight.BOLD, color=COLOR_PRIMARY),
            bgcolor=COLOR_SURFACE,
            padding=10,
            border_radius=5,
            on_click=self.toggle_language,
            ink=True,
            left=0, top=0,
            border=ft.Border.all(1, COLOR_PRIMARY)
        )

        self.header = ft.Container(
            content=ft.Stack([
                ft.Row([
                    ft.Column([
                        ft.Text(ui['title'], size=40, weight=ft.FontWeight.BOLD, color=COLOR_PRIMARY),
                        ft.Text(ui['subtitle'], size=16, color=ft.Colors.GREY_400),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                ], alignment=ft.MainAxisAlignment.CENTER),
                lang_btn
            ]),
            margin=ft.Margin.only(bottom=20)
        )

        self.main_content = ft.Column()
        self.show_categories(update=False)

        self.page.add(
            ft.Column([
                self.header,
                self.main_content,
                ft.Divider(color=COLOR_SURFACE),
                ft.Text(ui['footer'], size=12, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )
        self.page.update()

    def show_categories(self, update: bool = True):
        self.main_content.controls.clear()
        category_grid = ft.ResponsiveRow(spacing=20)

        for cat_key, info in CATEGORIES_INFO.items():
            name = info[self.lang]
            desc = info[f'desc_{self.lang}']
            category_grid.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Icon(info['icon'], size=40, color=info['color']),
                        ft.Text(name, size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Text(desc, size=16, color=ft.Colors.GREY_400, text_align=ft.TextAlign.CENTER),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=40, bgcolor=COLOR_SURFACE, border_radius=15, border=ft.Border.all(1, ft.Colors.GREY_800),
                    on_click=lambda e, k=cat_key: self.show_rule_selector(k),
                    col={"sm": 12, "md": 6}, ink=True
                )
            )

        self.main_content.controls.append(category_grid)
        if update:
            self.page.update()

    def show_rule_selector(self, category: str, update: bool = True):
        self.main_content.controls.clear()
        ui = LOCALIZED_UI[self.lang]

        back_button = ft.TextButton(ui['back_categories'], icon=ft.Icons.ARROW_BACK, on_click=lambda _: self.show_categories())
        rule_list = rules_by_category.get(category, [])

        grid = ft.Column(spacing=20)
        grid.controls.append(ft.Text(CATEGORIES_INFO[category][self.lang], size=24, weight=ft.FontWeight.BOLD, color=COLOR_PRIMARY))

        rule_grid = ft.ResponsiveRow(spacing=10)
        for rule in rule_list:
            rule_grid.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Text(rule.get_name(self.lang), weight=ft.FontWeight.BOLD, size=18, color=ft.Colors.WHITE),
                        ft.Text(rule.get_description(self.lang), size=14, color=ft.Colors.GREY_400),
                        ft.Text(rule.method, size=12, italic=True, color=COLOR_PRIMARY)
                    ]),
                    padding=20, bgcolor=COLOR_SURFACE, border_radius=10, border=ft.Border.all(1, ft.Colors.GREY_800),
                    on_click=lambda e, r=rule: self.select_rule(r),
                    col={"sm": 12, "md": 6, "lg": 4}, ink=True
                )
            )
        grid.controls.append(rule_grid)

        self.main_content.controls.append(back_button)
        self.main_content.controls.append(grid)
        if update:
            self.page.update()

    def select_rule(self, rule):
        self.selected_rule = rule
        self.show_mode_selection()

    def show_mode_selection(self, update: bool = True):
        self.main_content.controls.clear()
        ui = LOCALIZED_UI[self.lang]

        back_button = ft.TextButton(ui['back_methods'], icon=ft.Icons.ARROW_BACK, on_click=lambda _: self.show_rule_selector(self.selected_rule.category))

        cards = ft.ResponsiveRow([
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.SCHOOL, size=40, color=COLOR_PRIMARY),
                    ft.Text(ui['learn'], size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Text(ui['learn_desc'], size=16, color=ft.Colors.GREY_400),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=40, bgcolor=COLOR_SURFACE, border_radius=15, col={"sm": 12, "md": 6},
                on_click=lambda _: self.start_session("Learn"), ink=True, border=ft.Border.all(1, ft.Colors.GREY_800)
            ),
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.TIMER, size=40, color=COLOR_ACCENT),
                    ft.Text(ui['practice'], size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Text(ui['practice_desc'], size=16, color=ft.Colors.GREY_400),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=40, bgcolor=COLOR_SURFACE, border_radius=15, col={"sm": 12, "md": 6},
                on_click=lambda _: self.start_session("Practice"), ink=True, border=ft.Border.all(1, ft.Colors.GREY_800)
            )
        ], spacing=20)

        self.main_content.controls.append(back_button)
        self.main_content.controls.append(ft.Text(f"{ui['target']} {self.selected_rule.get_name(self.lang)}", size=20, weight=ft.FontWeight.BOLD, color=COLOR_PRIMARY))
        self.main_content.controls.append(cards)
        if update:
            self.page.update()

    def start_session(self, mode):
        self.mode = mode
        self.score = 0
        self.total = 0
        self.streak = 0
        self.start_time = time.time()
        self.timer_id += 1
        self.timer_running = True if mode == "Practice" else False
        self.show_practice_area()
        if mode == "Practice":
            self.page.run_task(self.update_timer, self.timer_id)

    async def update_timer(self, tid):
        ui = LOCALIZED_UI[self.lang]
        while self.timer_running and self.timer_id == tid:
            if self.start_time and hasattr(self, "timer_text"):
                try:
                    elapsed = int(time.time() - self.start_time)
                    mins, secs = divmod(elapsed, 60)
                    self.timer_text.value = f"{ui['time']} {mins:02d}:{secs:02d}"
                    self.timer_text.update()
                except: pass
            await asyncio.sleep(1)

    def show_practice_area(self, update: bool = True):
        self.main_content.controls.clear()
        ui = LOCALIZED_UI[self.lang]
        is_learn = (self.mode == "Learn")

        config_panel = ft.Column(visible=False)
        if not is_learn and self.selected_rule.id in ['tracht-addition', 'vedic-complementary-addition', 'vedic-subtraction-base']:
            self.num_operands_slider = ft.Slider(min=2, max=5, divisions=3, label=f"{ui['count']} {{value}}", value=2)
            self.num_digits_dropdown = ft.Dropdown(
                label=ui['digits'],
                options=[
                    ft.dropdown.Option("0", ui['random']),
                    ft.dropdown.Option("1", "1"),
                    ft.dropdown.Option("2", "2"),
                    ft.dropdown.Option("3", "3"),
                    ft.dropdown.Option("4", "4"),
                    ft.dropdown.Option("5", "5"),
                    ft.dropdown.Option("6", "6"),
                ],
                value="3"
            )

            config_panel.controls.extend([
                ft.Text(ui['custom_panel'], weight=ft.FontWeight.BOLD),
                ft.Row([
                    ft.Column([ft.Text(ui['count']), self.num_operands_slider]) if self.selected_rule.id != 'vedic-subtraction-base' else ft.Column(),
                    self.num_digits_dropdown
                ], alignment=ft.MainAxisAlignment.START),
                ft.Container(
                    content=ft.Text(ui['apply_restart'], weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    on_click=lambda _: self.page.run_task(self.next_problem),
                    height=45,
                    alignment=ft.Alignment.CENTER,
                    gradient=ft.LinearGradient([COLOR_PRIMARY, COLOR_ACCENT]),
                    border_radius=8,
                    ink=True
                ),
                ft.Divider(color=ft.Colors.GREY_800)
            ])
            config_panel.visible = True

        back_button = ft.TextButton(ui['back_methods'], icon=ft.Icons.ARROW_BACK, on_click=lambda _: self.show_mode_selection())

        # Problem Area Components
        self.problem_text = ft.Text("", size=48, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
        self.answer_input = ft.TextField(
            label=ui['enter_answer'], text_align=ft.TextAlign.CENTER,
            on_submit=self.handle_submit, keyboard_type=ft.KeyboardType.NUMBER, autofocus=True,
            border_color=COLOR_PRIMARY, cursor_color=COLOR_ACCENT
        )
        self.feedback_text = ft.Text("", size=18, weight=ft.FontWeight.BOLD)
        self.score_text = ft.Text(f"{ui['score']} 0/0", size=16, visible=not is_learn, color=ft.Colors.WHITE)
        self.streak_text = ft.Text(f"{ui['streak']} 0", size=16, color=COLOR_ACCENT, weight=ft.FontWeight.BOLD, visible=not is_learn)
        self.timer_text = ft.Text(f"{ui['time']} 00:00", size=16, visible=not is_learn, color=ft.Colors.GREY_400)

        self.check_button = ft.Container(
            content=ft.Text(ui['check'], weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            on_click=self.check_answer,
            width=400,
            height=50,
            alignment=ft.Alignment.CENTER,
            gradient=ft.LinearGradient([COLOR_PRIMARY, COLOR_ACCENT]),
            border_radius=10,
            ink=True
        )
        self.next_button = ft.Container(
            content=ft.Text(ui['next'], weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            on_click=self.next_problem,
            width=400,
            height=50,
            alignment=ft.Alignment.CENTER,
            gradient=ft.LinearGradient([ft.Colors.GREEN_400, ft.Colors.GREEN_700]),
            border_radius=10,
            ink=True,
            visible=False
        )

        self.practice_card = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Column([ft.Text(self.selected_rule.get_name(self.lang), weight=ft.FontWeight.BOLD, color=COLOR_PRIMARY), self.timer_text]),
                    ft.Column([self.score_text, self.streak_text], horizontal_alignment=ft.CrossAxisAlignment.END)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Divider(color=ft.Colors.GREY_800),
                ft.Column([self.problem_text, ft.Text("= ?", size=20, color=ft.Colors.GREY_600)], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                self.answer_input, self.check_button, self.next_button, self.feedback_text,
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
            padding=30, bgcolor=COLOR_SURFACE, border_radius=15, border=ft.Border.all(1, ft.Colors.GREY_800)
        )

        # Theory & Steps Area
        self.steps_column = ft.Column(spacing=10)
        theory_card = ft.Container(
            content=ft.Column([
                ft.Text(ui['theory_title'], size=24, weight=ft.FontWeight.BOLD, color=COLOR_PRIMARY),
                ft.Text(self.selected_rule.get_explanation(self.lang), size=16, color=ft.Colors.GREY_400),
                ft.Text(ui['example_title'], size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Container(content=ft.Text(self.selected_rule.get_example(self.lang), font_family="monospace", size=14, color=ft.Colors.WHITE),
                             padding=15, bgcolor=COLOR_BG, border_radius=10, border=ft.Border.all(1, ft.Colors.GREY_800)),
                ft.Column([
                    ft.Divider(color=ft.Colors.GREY_800),
                    ft.Text(ui['steps_title'], size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_400),
                    self.steps_column
                ], visible=is_learn)
            ], spacing=15),
            padding=30, bgcolor=COLOR_SURFACE, border_radius=15, border=ft.Border.all(1, ft.Colors.GREY_800)
        )

        self.main_content.controls.append(back_button)
        if config_panel.visible:
            self.main_content.controls.append(config_panel)

        # In Learn mode, theory is at the top. In Practice, it might be on the side/bottom.
        if is_learn:
            self.main_content.controls.append(theory_card)
            self.main_content.controls.append(ft.Container(height=20))
            self.main_content.controls.append(self.practice_card)
        else:
            self.main_content.controls.append(
                ft.ResponsiveRow([
                    ft.Column([self.practice_card], col={"lg": 6}),
                    ft.Column([theory_card], col={"lg": 6})
                ])
            )

        if update:
            self.page.update()
        self.page.run_task(self.next_problem)

    async def next_problem(self, e=None):
        try:
            kwargs = {}
            if hasattr(self, 'num_operands_slider'):
                kwargs['num_operands'] = int(self.num_operands_slider.value)
            if hasattr(self, 'num_digits_dropdown'):
                kwargs['num_digits'] = int(self.num_digits_dropdown.value)
            self.current_problem = self.selected_rule.generate_problem(**kwargs)
        except:
            self.current_problem = {"question": "Error", "answer": 0}

        self.problem_text.value = to_lang_digits(self.current_problem["question"], self.lang)
        self.answer_input.value = ""
        self.answer_input.disabled = False
        self.feedback_text.value = ""
        self.check_button.visible = True
        self.next_button.visible = False

        # Update steps in Learn mode
        if self.mode == "Learn":
            self.steps_column.controls.clear()
            steps = self.selected_rule.get_steps(self.current_problem, self.lang)
            for step in steps:
                self.steps_column.controls.append(ft.Text(step, size=14, color=ft.Colors.GREY_400))

        self.page.update()
        await self.answer_input.focus()

    async def handle_submit(self, e):
        if self.check_button.visible: await self.check_answer(e)
        else: await self.next_problem()

    async def check_answer(self, e):
        if not self.answer_input.value: return
        ui = LOCALIZED_UI[self.lang]
        try: user_val = int(self.answer_input.value)
        except: return

        self.total += 1
        if user_val == self.current_problem["answer"]:
            self.score += 1
            self.streak += 1
            self.feedback_text.value = ui['correct']
            self.feedback_text.color = COLOR_SUCCESS
        else:
            self.streak = 0
            ans_str = to_lang_digits(self.current_problem['answer'], self.lang)
            self.feedback_text.value = f"{ui['wrong']} {ans_str}"
            self.feedback_text.color = ft.Colors.RED_400

        self.score_text.value = f"{ui['score']} {to_lang_digits(self.score, self.lang)}/{to_lang_digits(self.total, self.lang)}"
        self.streak_text.value = f"{ui['streak']} {to_lang_digits(self.streak, self.lang)}"
        self.answer_input.disabled = True
        self.check_button.visible = False
        self.next_button.visible = True
        self.page.update()

def main(page: ft.Page):
    FastMathApp(page)

if __name__ == "__main__":
    ft.app(target=main)
