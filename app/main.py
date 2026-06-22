import flet as ft
import time
import asyncio
import random
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

import json
from datetime import datetime

# Theme Colors
COLOR_PRIMARY = "#00EEFF"  # Electric Blue
COLOR_ACCENT = "#FF6B00"   # Bright Orange
COLOR_BG = "#050A18"       # Deep Dark
COLOR_SURFACE = "#161B22"  # Dark Surface
COLOR_SUCCESS = "#00FF7F"  # Spring Green

LOCALIZED_UI = {
    'en': {
        'title': 'MathBeast',
        'subtitle': 'Master Rapid Calculation',
        'back_systems': 'Back to Systems',
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
        'choose_system': 'Choose a Calculation System',
        'trachtenberg': 'Trachtenberg System',
        'vedic': 'Vedic Mathematics',
        'stats_title': 'Statistics',
        'level': 'Level',
        'xp': 'XP',
        'daily_challenge': 'Daily Challenge',
        'solved': 'solved',
        'continue_training': 'Continue Training',
        'accuracy': 'Accuracy',
        'avg_time': 'Avg Time',
        'fastest': 'Fastest',
        'best_streak': 'Best Streak',
        'total_xp': 'Total XP',
        'xp_today': 'XP Today',
        'combo': 'COMBO',
        'perfect': 'PERFECT!',
        'arena': 'ARENA',
        'back': 'Back',
        'footer': '© 2024 MathBeast. Built with Flet.'
    },
    'fa': {
        'title': 'MathBeast',
        'subtitle': 'تسلط بر محاسبات ذهنی سریع',
        'back_systems': 'بازگشت به سیستم‌ها',
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
        'choose_system': 'انتخاب سیستم محاسباتی',
        'trachtenberg': 'سیستم تراختنبرگ',
        'vedic': 'ریاضیات وِدیک',
        'stats_title': 'آمار و ارقام',
        'level': 'سطح',
        'xp': 'امتیاز (XP)',
        'daily_challenge': 'چالش روزانه',
        'solved': 'حل شده',
        'continue_training': 'ادامه آموزش',
        'accuracy': 'دقت',
        'avg_time': 'میانگین زمان',
        'fastest': 'سریع‌ترین',
        'best_streak': 'بهترین توالی',
        'total_xp': 'کل امتیاز',
        'xp_today': 'امتیاز امروز',
        'combo': 'توالی',
        'perfect': 'عالی!',
        'arena': 'میدان مبارزه',
        'back': 'بازگشت',
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

class MathBeast:
    def __init__(self, page: ft.Page):
        self.page = page
        self.lang = 'fa'
        self.current_problem = None
        self.update_page_config()

        self.selected_rule = None
        self.current_problem = None
        self.score = 0
        self.total = 0
        self.streak = 0
        self.start_time = None
        self.timer_running = False
        self.timer_id = 0
        self.mode = None
        self.selected_system = None

        # Beast Mascot & Progress State
        self.total_xp = 0
        self.xp_today = 0
        self.daily_solved_count = 0
        self.best_streak = 0
        self.solve_times = []  # To track average/fastest
        self.last_solve_date = ""

        self.load_state()
        self.check_daily_reset()
        self.setup_ui()

    def load_state(self):
        try:
            stored_state = self.page.client_storage.get("mathbeast_state")
            if stored_state:
                data = json.loads(stored_state)
                self.total_xp = data.get("total_xp", 0)
                self.xp_today = data.get("xp_today", 0)
                self.daily_solved_count = data.get("daily_solved_count", 0)
                self.best_streak = data.get("best_streak", 0)
                self.solve_times = data.get("solve_times", [])
                self.last_solve_date = data.get("last_solve_date", "")
        except Exception as e:
            print(f"Error loading state: {e}")

    def save_state(self):
        try:
            state = {
                "total_xp": self.total_xp,
                "xp_today": self.xp_today,
                "daily_solved_count": self.daily_solved_count,
                "best_streak": self.best_streak,
                "solve_times": self.solve_times,
                "last_solve_date": self.last_solve_date
            }
            self.page.client_storage.set("mathbeast_state", json.dumps(state))
        except Exception as e:
            print(f"Error saving state: {e}")

    def check_daily_reset(self):
        today = datetime.now().strftime("%Y-%m-%d")
        if self.last_solve_date != today:
            self.xp_today = 0
            self.daily_solved_count = 0
            self.last_solve_date = today
            self.save_state()

    def reset_progress(self, e):
        def confirm_reset(e):
            self.total_xp = 0
            self.xp_today = 0
            self.daily_solved_count = 0
            self.best_streak = 0
            self.solve_times = []
            self.last_solve_date = datetime.now().strftime("%Y-%m-%d")
            self.save_state()
            self.page.dialog.open = False
            self.show_statistics()

        def cancel_reset(e):
            self.page.dialog.open = False
            self.page.update()

        self.page.dialog = ft.AlertDialog(
            title=ft.Text("Reset Progress?" if self.lang == 'en' else "بازنشانی پیشرفت؟"),
            content=ft.Text("This will wipe all your XP and statistics permanently." if self.lang == 'en' else "این کار تمام امتیازات و آمار شما را برای همیشه پاک می‌کند."),
            actions=[
                ft.TextButton("Yes" if self.lang == 'en' else "بله", on_click=confirm_reset),
                ft.TextButton("No" if self.lang == 'en' else "خیر", on_click=cancel_reset),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.page.dialog.open = True
        self.page.update()

    def get_beast_state(self):
        level = (self.total_xp // 100) + 1
        if self.total_xp >= 5000:
            state = "Math Titan" if self.lang == 'en' else "تایتان ریاضی"
            mascot = "🐉"
        elif self.total_xp >= 1000:
            state = "Alpha Beast" if self.lang == 'en' else "هیولای آلفا"
            mascot = "🦍"
        elif self.total_xp >= 500:
            state = "Warrior Beast" if self.lang == 'en' else "هیولای جنگجو"
            mascot = "🦁"
        elif self.total_xp >= 100:
            state = "Young Beast" if self.lang == 'en' else "هیولای جوان"
            mascot = "🐺"
        else:
            state = "Cub" if self.lang == 'en' else "توله هیولا"
            mascot = "🐾"
        return level, state, mascot

    def show_statistics(self, update: bool = True):
        ui = LOCALIZED_UI[self.lang]
        accuracy = (self.score / self.total * 100) if self.total > 0 else 0
        avg_time = sum(self.solve_times) / len(self.solve_times) if self.solve_times else 0
        fastest = min(self.solve_times) if self.solve_times else 0
        level, state, mascot = self.get_beast_state()

        back_btn = ft.TextButton(ui['back'], icon=ft.Icons.ARROW_BACK, on_click=lambda _: self.show_system_selection())

        def stat_card(label, value, icon, color):
            return ft.Container(
                content=ft.Column([
                    ft.Icon(icon, color=color, size=30),
                    ft.Text(label, size=14, color=ft.Colors.GREY_400),
                    ft.Text(value, size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=20, bgcolor=COLOR_SURFACE, border_radius=15, col={"sm": 6, "md": 4}
            )

        view = ft.Column([
            ft.Row([back_btn], alignment=ft.MainAxisAlignment.START),
            ft.Text(ui['stats_title'], size=32, weight=ft.FontWeight.BOLD, color=COLOR_PRIMARY),
            ft.Container(height=20),
            ft.ResponsiveRow([
                stat_card(ui['accuracy'], f"{to_lang_digits(int(accuracy), self.lang)}%", ft.Icons.TRACK_CHANGES, ft.Colors.GREEN_400),
                stat_card(ui['avg_time'], f"{to_lang_digits(round(avg_time, 1), self.lang)}s", ft.Icons.TIMER, ft.Colors.BLUE_400),
                stat_card(ui['fastest'], f"{to_lang_digits(round(fastest, 1), self.lang)}s", ft.Icons.BOLT, COLOR_ACCENT),
                stat_card(ui['best_streak'], to_lang_digits(self.best_streak, self.lang), ft.Icons.STAR, ft.Colors.YELLOW_400),
                stat_card(ui['total_xp'], to_lang_digits(self.total_xp, self.lang), ft.Icons.UPGRADE, COLOR_PRIMARY),
                stat_card(ui['xp_today'], to_lang_digits(self.xp_today, self.lang), ft.Icons.TODAY, ft.Colors.PURPLE_400),
            ], spacing=10),
            ft.Container(height=30),
            ft.Text(f"{mascot} {state}", size=20, color=COLOR_PRIMARY, weight=ft.FontWeight.BOLD),
            ft.Container(height=20),
            ft.ElevatedButton("Reset Progress" if self.lang == 'en' else "بازنشانی پیشرفت",
                             icon=ft.Icons.DELETE_FOREVER,
                             color=ft.Colors.WHITE,
                             bgcolor=ft.Colors.RED_700,
                             on_click=self.reset_progress)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        self.main_content.content = view
        if update:
            self.page.update()

    def update_page_config(self):
        self.page.title = LOCALIZED_UI[self.lang]['title']
        self.page.rtl = (self.lang == 'fa')
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.padding = 0
        self.page.bgcolor = COLOR_BG
        self.page.scroll = ft.ScrollMode.HIDDEN

    def toggle_language(self, e):
        self.lang = 'en' if self.lang == 'fa' else 'fa'
        self.update_page_config()
        # Full UI refresh
        self.page.controls.clear()
        self.setup_ui()

    def create_background(self):
        symbols = ["Σ", "π", "∞", "√", "÷", "×", "+", "-", "=", "%", "Δ", "Ω", "∫", "≈"]
        particles = []
        for _ in range(25):
            particles.append(
                ft.Container(
                    content=ft.Text(
                        random.choice(symbols),
                        size=random.randint(20, 60),
                        color=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
                        weight=ft.FontWeight.BOLD
                    ),
                    left=random.randint(0, 1800),
                    top=random.randint(0, 1200),
                    rotate=ft.Rotate(random.uniform(0, 6.28))
                )
            )
        return ft.Stack(particles, expand=True)

    def on_hover(self, e):
        e.control.scale = 1.05 if e.data == "true" else 1.0
        e.control.border = ft.Border.all(2, COLOR_PRIMARY) if e.data == "true" else ft.Border.all(1, ft.Colors.with_opacity(0.1, ft.Colors.WHITE))
        if e.data == "true":
            e.control.shadow = ft.BoxShadow(blur_radius=20, color=ft.Colors.with_opacity(0.2, COLOR_PRIMARY))
        else:
            e.control.shadow = None
        e.control.update()

    def on_hover_btn(self, e, color):
        e.control.scale = 1.05 if e.data == "true" else 1.0
        if e.data == "true":
            e.control.shadow = ft.BoxShadow(blur_radius=25, color=ft.Colors.with_opacity(0.5, color))
        else:
            e.control.shadow = ft.BoxShadow(blur_radius=15, color=ft.Colors.with_opacity(0.3, color))
        e.control.update()

    def setup_ui(self):
        ui = LOCALIZED_UI[self.lang]

        lang_btn = ft.Container(
            content=ft.Text("en" if self.lang == 'fa' else "فا", weight=ft.FontWeight.BOLD, color=COLOR_PRIMARY),
            bgcolor=ft.Colors.with_opacity(0.1, COLOR_PRIMARY),
            padding=10,
            border_radius=10,
            on_click=self.toggle_language,
            ink=True,
            left=20, top=20,
            border=ft.Border.all(1, ft.Colors.with_opacity(0.3, COLOR_PRIMARY)),
            blur=5,
            on_hover=lambda e: self.on_hover_btn(e, COLOR_PRIMARY)
        )

        self.header = ft.Container(
            content=ft.Column([
                ft.Text(ui['title'], size=50, weight=ft.FontWeight.BOLD, color=COLOR_PRIMARY),
                ft.Text(ui['subtitle'], size=18, color=ft.Colors.GREY_400, italic=True),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            margin=ft.Margin.only(bottom=40, top=40)
        )

        self.main_content = ft.AnimatedSwitcher(
            content=ft.Column(),
            transition=ft.AnimatedSwitcherTransition.FADE,
            duration=400,
            reverse_duration=300,
            switch_in_curve=ft.AnimationCurve.EASE_OUT,
            expand=True
        )

        self.root_container = ft.Container(
            content=ft.Stack([
                self.create_background(),
                ft.Column([
                    ft.Column([
                        self.header,
                        self.main_content,
                        ft.Divider(color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE), height=60),
                        ft.Text(ui['footer'], size=12, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER),
                        ft.Container(height=40)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True, scroll=ft.ScrollMode.AUTO),
                ], expand=True),
                lang_btn
            ]),
            expand=True,
            gradient=ft.LinearGradient(
                begin=ft.Alignment.TOP_LEFT,
                end=ft.Alignment.BOTTOM_RIGHT,
                colors=[COLOR_BG, "#1E293B"]
            )
        )

        self.page.add(self.root_container)

        # Route back to current view
        if self.selected_rule and (self.mode == "Learn" or self.mode == "Practice"):
            self.show_practice_area(update=False, skip_next_problem=True)
            if self.current_problem:
                self.problem_text.value = to_lang_digits(self.current_problem["question"], self.lang)
        elif self.selected_rule:
            self.show_mode_selection(update=False)
        elif self.selected_system:
            self.show_categories(update=False)
        else:
            self.show_system_selection(update=False)

        self.page.update()

    def show_system_selection(self, update: bool = True):
        ui = LOCALIZED_UI[self.lang]
        level, state, mascot = self.get_beast_state()

        # Hero Section
        hero = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(mascot, size=80),
                    ft.Column([
                        ft.Text(f"{ui['level']} {to_lang_digits(level, self.lang)} {state}", size=24, weight=ft.FontWeight.BOLD, color=COLOR_PRIMARY),
                        ft.Text(f"{ui['xp']}: {to_lang_digits(self.total_xp, self.lang)} / {to_lang_digits(((level)*100), self.lang)}", size=16, color=ft.Colors.GREY_400),
                        ft.ProgressBar(value=self.total_xp % 100 / 100, width=300, color=COLOR_PRIMARY, bgcolor=ft.Colors.with_opacity(0.1, COLOR_PRIMARY)),
                    ], spacing=5)
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                ft.Container(height=10),
                ft.Row([
                    ft.Icon(ft.Icons.CALENDAR_TODAY, color=COLOR_ACCENT, size=20),
                    ft.Text(f"{ui['daily_challenge']}: {to_lang_digits(self.daily_solved_count, self.lang)} / {to_lang_digits(20, self.lang)} {ui['solved']}", size=14, color=ft.Colors.GREY_300),
                ], alignment=ft.MainAxisAlignment.CENTER),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=30,
            bgcolor=ft.Colors.with_opacity(0.05, COLOR_PRIMARY),
            border_radius=30,
            border=ft.Border.all(1, ft.Colors.with_opacity(0.1, COLOR_PRIMARY)),
            margin=ft.Margin.only(bottom=30)
        )

        stats_btn = ft.Container(
            content=ft.Row([ft.Icon(ft.Icons.BAR_CHART), ft.Text(ui['stats_title'], weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.CENTER),
            padding=15, border_radius=15, bgcolor=COLOR_SURFACE,
            border=ft.Border.all(1, ft.Colors.with_opacity(0.1, ft.Colors.WHITE)),
            on_click=lambda _: self.show_statistics(), ink=True,
            on_hover=self.on_hover
        )

        cards = ft.ResponsiveRow([
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.AUTO_AWESOME_MOTION, size=40, color=COLOR_PRIMARY),
                    ft.Text(ui['trachtenberg'], size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Text("Speed system for multiplication and addition.", size=16, color=ft.Colors.GREY_400, text_align=ft.TextAlign.CENTER),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=40, bgcolor=COLOR_SURFACE, border_radius=20, col={"sm": 12, "md": 6},
                on_click=lambda _: self.select_system("Trachtenberg"), ink=True,
                on_hover=self.on_hover, animate=ft.Animation(300, ft.AnimationCurve.DECELERATE),
                border=ft.Border.all(1, ft.Colors.with_opacity(0.1, ft.Colors.WHITE))
            ),
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.HUB, size=40, color=COLOR_ACCENT),
                    ft.Text(ui['vedic'], size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Text("Ancient Indian mathematical techniques.", size=16, color=ft.Colors.GREY_400, text_align=ft.TextAlign.CENTER),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=40, bgcolor=COLOR_SURFACE, border_radius=20, col={"sm": 12, "md": 6},
                on_click=lambda _: self.select_system("Vedic"), ink=True,
                on_hover=self.on_hover, animate=ft.Animation(300, ft.AnimationCurve.DECELERATE),
                border=ft.Border.all(1, ft.Colors.with_opacity(0.1, ft.Colors.WHITE))
            )
        ], spacing=20)

        view = ft.Column([
            hero,
            ft.Row([stats_btn], alignment=ft.MainAxisAlignment.CENTER),
            ft.Container(height=20),
            ft.Text(ui['choose_system'], size=28, weight=ft.FontWeight.BOLD, color=COLOR_PRIMARY),
            ft.Container(height=10),
            cards
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        self.main_content.content = view
        if update:
            self.page.update()

    def select_system(self, system):
        self.selected_system = system
        self.show_categories()

    def show_categories(self, update: bool = True):
        ui = LOCALIZED_UI[self.lang]

        back_button = ft.TextButton(ui['back_systems'],
                                    icon=ft.Icons.ARROW_BACK, on_click=lambda _: self.show_system_selection())

        category_grid = ft.ResponsiveRow(spacing=20)

        for cat_key, info in CATEGORIES_INFO.items():
            # Filter categories by selected system
            cat_rules = [r for r in rules_by_category.get(cat_key, []) if r.method == self.selected_system]
            if not cat_rules:
                continue

            name = info[self.lang]
            desc = info[f'desc_{self.lang}']
            category_grid.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Icon(info['icon'], size=40, color=info['color']),
                        ft.Text(name, size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Text(desc, size=16, color=ft.Colors.GREY_400, text_align=ft.TextAlign.CENTER),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=40, bgcolor=COLOR_SURFACE, border_radius=20,
                    border=ft.Border.all(1, ft.Colors.with_opacity(0.1, ft.Colors.WHITE)),
                    on_click=lambda e, k=cat_key: self.show_rule_selector(k),
                    on_hover=self.on_hover, animate=ft.Animation(300, ft.AnimationCurve.DECELERATE),
                    col={"sm": 12, "md": 6}, ink=True
                )
            )

        view = ft.Column([
            ft.Row([back_button], alignment=ft.MainAxisAlignment.START),
            ft.Text(f"{self.selected_system}", size=32, weight=ft.FontWeight.BOLD, color=COLOR_ACCENT),
            ft.Container(height=10),
            category_grid
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        self.main_content.content = view
        if update:
            self.page.update()

    def show_rule_selector(self, category: str, update: bool = True):
        ui = LOCALIZED_UI[self.lang]

        back_button = ft.TextButton(ui['back_categories'], icon=ft.Icons.ARROW_BACK, on_click=lambda _: self.show_categories())
        # Filter rules by selected system
        rule_list = [r for r in rules_by_category.get(category, []) if r.method == self.selected_system]

        rule_grid = ft.ResponsiveRow(spacing=10)
        for rule in rule_list:
            rule_grid.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Text(rule.get_name(self.lang), weight=ft.FontWeight.BOLD, size=18, color=ft.Colors.WHITE),
                        ft.Text(rule.get_description(self.lang), size=14, color=ft.Colors.GREY_400),
                        ft.Text(rule.method, size=12, italic=True, color=COLOR_PRIMARY)
                    ]),
                    padding=20, bgcolor=COLOR_SURFACE, border_radius=15,
                    border=ft.Border.all(1, ft.Colors.with_opacity(0.1, ft.Colors.WHITE)),
                    on_click=lambda e, r=rule: self.select_rule(r),
                    on_hover=self.on_hover, animate=ft.Animation(300, ft.AnimationCurve.DECELERATE),
                    col={"sm": 12, "md": 6, "lg": 4}, ink=True
                )
            )

        view = ft.Column([
            ft.Row([back_button], alignment=ft.MainAxisAlignment.START),
            ft.Text(CATEGORIES_INFO[category][self.lang], size=28, weight=ft.FontWeight.BOLD, color=COLOR_PRIMARY),
            ft.Container(height=10),
            rule_grid
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        self.main_content.content = view
        if update:
            self.page.update()

    def select_rule(self, rule):
        self.selected_rule = rule
        self.show_mode_selection()

    def show_mode_selection(self, update: bool = True):
        ui = LOCALIZED_UI[self.lang]

        back_button = ft.TextButton(ui['back_methods'], icon=ft.Icons.ARROW_BACK, on_click=lambda _: self.show_rule_selector(self.selected_rule.category))

        cards = ft.ResponsiveRow([
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.SCHOOL, size=40, color=COLOR_PRIMARY),
                    ft.Text(ui['learn'], size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Text(ui['learn_desc'], size=16, color=ft.Colors.GREY_400, text_align=ft.TextAlign.CENTER),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=40, bgcolor=COLOR_SURFACE, border_radius=20,
                border=ft.Border.all(1, ft.Colors.with_opacity(0.1, ft.Colors.WHITE)),
                on_click=lambda _: self.start_session("Learn"), ink=True,
                on_hover=self.on_hover, animate=ft.Animation(300, ft.AnimationCurve.DECELERATE),
                col={"sm": 12, "md": 6}
            ),
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.TIMER, size=40, color=COLOR_ACCENT),
                    ft.Text(ui['practice'], size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Text(ui['practice_desc'], size=16, color=ft.Colors.GREY_400, text_align=ft.TextAlign.CENTER),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=40, bgcolor=COLOR_SURFACE, border_radius=20,
                border=ft.Border.all(1, ft.Colors.with_opacity(0.1, ft.Colors.WHITE)),
                on_click=lambda _: self.start_session("Practice"), ink=True,
                on_hover=self.on_hover, animate=ft.Animation(300, ft.AnimationCurve.DECELERATE),
                col={"sm": 12, "md": 6}
            )
        ], spacing=20)

        view = ft.Column([
            ft.Row([back_button], alignment=ft.MainAxisAlignment.START),
            ft.Text(f"{ui['target']} {self.selected_rule.get_name(self.lang)}", size=24, weight=ft.FontWeight.BOLD, color=COLOR_PRIMARY),
            ft.Container(height=10),
            cards
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        self.main_content.content = view
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
                    if self.timer_text.page:
                        self.timer_text.update()

                    # Update Arena Ring (deplete over 30s as a visual goal)
                    if hasattr(self, "arena_timer"):
                        # We use problem_start_time for per-problem ring
                        if hasattr(self, "problem_start_time"):
                            p_elapsed = time.time() - self.problem_start_time
                            self.arena_timer.value = max(0, 1 - (p_elapsed / 30))
                            if self.arena_timer.page:
                                self.arena_timer.update()
                except Exception as e:
                    print(f"Error in update_timer: {e}")
            await asyncio.sleep(0.1)

    def trigger_success_animation(self, combo=1):
        ui = LOCALIZED_UI[self.lang]
        # Combo/XP indicator
        xp_gain = 10 + (combo * 5)
        indicator = ft.Container(
            content=ft.Column([
                ft.Text(f"✓ {ui['perfect']}", color=COLOR_SUCCESS, size=24, weight=ft.FontWeight.BOLD),
                ft.Text(f"+{to_lang_digits(xp_gain, self.lang)} {ui['xp']}", color=COLOR_PRIMARY, size=18, weight=ft.FontWeight.BOLD),
                ft.Text(f"{to_lang_digits(combo, self.lang)}x {ui['combo']}", color=COLOR_ACCENT, size=16, weight=ft.FontWeight.BOLD) if combo > 1 else ft.Container()
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            left=self.page.width/2 - 50,
            top=self.page.height/2 - 150,
            animate_opacity=ft.Animation(800, ft.AnimationCurve.EASE_IN_OUT),
            animate_offset=ft.Animation(800, ft.AnimationCurve.EASE_OUT),
            offset=ft.Offset(0, 0),
            opacity=1
        )
        self.page.overlay.append(indicator)
        self.page.update()

        indicator.offset = ft.Offset(0, -1)
        indicator.opacity = 0
        indicator.update()

        async def remove_indicator(ind):
            await asyncio.sleep(1)
            if ind in self.page.overlay:
                self.page.overlay.remove(ind)
                self.page.update()
        self.page.run_task(remove_indicator, indicator)

        for _ in range(15):
            star = ft.Icon(
                name=ft.Icons.STAR,
                color=ft.Colors.YELLOW_400 if random.random() > 0.5 else COLOR_SUCCESS,
                size=random.randint(10, 30),
                opacity=1,
                left=random.randint(100, 1500),
                top=random.randint(100, 800),
                scale=0,
                animate_scale=ft.Animation(600, ft.AnimationCurve.BOUNCE_OUT),
                animate_opacity=ft.Animation(1000, ft.AnimationCurve.EASE_OUT)
            )
            self.page.overlay.append(star)
            self.page.update()
            star.scale = 1
            star.update()

            async def remove_star(s=star):
                await asyncio.sleep(1)
                s.opacity = 0
                s.update()
                await asyncio.sleep(1)
                self.page.overlay.remove(s)
                self.page.update()

            self.page.run_task(remove_star)

    def show_practice_area(self, update: bool = True, skip_next_problem: bool = False):
        if not self.selected_rule:
            self.show_system_selection()
            return
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
                    border_radius=10,
                    ink=True,
                    on_hover=lambda e: self.on_hover_btn(e, COLOR_PRIMARY)
                ),
                ft.Divider(color=ft.Colors.GREY_800)
            ])
            config_panel.visible = True

        back_button = ft.TextButton(ui['back_methods'], icon=ft.Icons.ARROW_BACK, on_click=lambda _: self.show_mode_selection())

        self.fallback_note = ft.Text(
            "Note: with these settings this becomes standard addition" if self.lang == 'en' else "توجه: با این تنظیمات، این مسئله تبدیل به جمع معمولی می‌شود",
            color=COLOR_ACCENT, size=14, italic=True, visible=False
        )

        # Problem Area Components
        self.arena_timer = ft.ProgressRing(value=1.0, width=200, height=200, stroke_width=10, color=COLOR_PRIMARY, bgcolor=ft.Colors.with_opacity(0.1, COLOR_PRIMARY))
        self.problem_text = ft.Text("", size=60, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, rtl=False,
                                   animate_scale=ft.Animation(400, ft.AnimationCurve.BOUNCE_OUT), scale=1)

        self.arena_stack = ft.Stack([
            ft.Container(self.arena_timer, alignment=ft.Alignment.CENTER),
            ft.Container(self.problem_text, alignment=ft.Alignment.CENTER),
        ], width=250, height=250)

        self.answer_input = ft.TextField(
            label=ui['enter_answer'], text_align=ft.TextAlign.CENTER,
            on_submit=self.handle_submit, keyboard_type=ft.KeyboardType.NUMBER, autofocus=True,
            border_color=COLOR_PRIMARY, cursor_color=COLOR_ACCENT,
            animate_offset=ft.Animation(100, ft.AnimationCurve.BOUNCE_IN),
            offset=ft.Offset(0, 0)
        )
        self.feedback_text = ft.Text("", size=18, weight=ft.FontWeight.BOLD,
                                    animate_opacity=ft.Animation(300, ft.AnimationCurve.EASE_IN))
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
            border_radius=15,
            ink=True,
            shadow=ft.BoxShadow(blur_radius=15, color=ft.Colors.with_opacity(0.3, COLOR_PRIMARY)),
            on_hover=lambda e: self.on_hover_btn(e, COLOR_PRIMARY)
        )
        self.next_button = ft.Container(
            content=ft.Text(ui['next'], weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            on_click=self.next_problem,
            width=400,
            height=50,
            alignment=ft.Alignment.CENTER,
            gradient=ft.LinearGradient([ft.Colors.GREEN_400, ft.Colors.GREEN_700]),
            border_radius=15,
            ink=True,
            visible=False,
            shadow=ft.BoxShadow(blur_radius=15, color=ft.Colors.with_opacity(0.3, ft.Colors.GREEN_700)),
            on_hover=lambda e: self.on_hover_btn(e, ft.Colors.GREEN_700)
        )

        self.practice_card = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Column([ft.Text(self.selected_rule.get_name(self.lang), weight=ft.FontWeight.BOLD, color=COLOR_PRIMARY, size=18), self.timer_text]),
                    ft.Column([self.score_text, self.streak_text], horizontal_alignment=ft.CrossAxisAlignment.END)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Divider(color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE)),
                ft.Text(ui['arena'], size=12, weight=ft.FontWeight.BOLD, color=ft.Colors.with_opacity(0.3, COLOR_PRIMARY)),
                self.arena_stack,
                ft.Text("= ?", size=20, color=ft.Colors.GREY_600),
                self.answer_input, self.check_button, self.next_button, self.feedback_text,
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
            padding=40, bgcolor=COLOR_SURFACE, border_radius=20,
            border=ft.Border.all(1, ft.Colors.with_opacity(0.1, ft.Colors.WHITE)),
            shadow=ft.BoxShadow(blur_radius=30, color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK))
        )

        # Theory & Steps Area
        self.steps_column = ft.Column(spacing=10)
        theory_card = ft.Container(
            content=ft.Column([
                ft.Text(ui['theory_title'], size=24, weight=ft.FontWeight.BOLD, color=COLOR_PRIMARY),
                ft.Text(self.selected_rule.get_explanation(self.lang), size=16, color=ft.Colors.GREY_400),
                ft.Text(ui['example_title'], size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Container(content=ft.Text(self.selected_rule.get_example(self.lang), font_family="monospace", size=14, color=ft.Colors.WHITE),
                             padding=15, bgcolor=COLOR_BG, border_radius=15,
                             border=ft.Border.all(1, ft.Colors.with_opacity(0.1, ft.Colors.WHITE))),
                ft.Column([
                    ft.Divider(color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE)),
                    ft.Text(ui['steps_title'], size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_400),
                    self.steps_column
                ], visible=is_learn)
            ], spacing=15),
            padding=30, bgcolor=COLOR_SURFACE, border_radius=20,
            border=ft.Border.all(1, ft.Colors.with_opacity(0.1, ft.Colors.WHITE))
        )

        content_list = [
            ft.Row([back_button], alignment=ft.MainAxisAlignment.START),
            self.fallback_note
        ]
        if config_panel.visible:
            content_list.append(config_panel)

        # In Learn mode, theory is at the top. In Practice, it might be on the side/bottom.
        if is_learn:
            content_list.extend([
                theory_card,
                ft.Container(height=20),
                self.practice_card
            ])
        else:
            content_list.append(
                ft.ResponsiveRow([
                    ft.Column([self.practice_card], col={"lg": 6}),
                    ft.Column([theory_card], col={"lg": 6})
                ])
            )

        view = ft.Column(content_list, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        self.main_content.content = view

        if update:
            self.page.update()
        if not skip_next_problem:
            self.page.run_task(self.next_problem)

    async def next_problem(self, e=None):
        self.problem_start_time = time.time()
        if hasattr(self, "arena_timer"):
            self.arena_timer.value = 1.0
            self.arena_timer.color = COLOR_PRIMARY
            try:
                if self.arena_timer.page:
                    self.arena_timer.update()
            except: pass

        self.problem_text.scale = 0.8
        try:
            if self.problem_text.page:
                self.problem_text.update()
        except: pass
        try:
            kwargs = {}
            if hasattr(self, 'num_operands_slider'):
                kwargs['num_operands'] = int(self.num_operands_slider.value)
            if hasattr(self, 'num_digits_dropdown'):
                kwargs['num_digits'] = int(self.num_digits_dropdown.value)
            self.current_problem = self.selected_rule.generate_problem(**kwargs)
            if self.selected_rule.id == 'vedic-complementary-addition':
                if kwargs.get('num_operands', 2) > 2 or kwargs.get('num_digits', 3) != 3:
                    self.fallback_note.visible = True
                else:
                    self.fallback_note.visible = False
                try:
                    if self.fallback_note.page:
                        self.fallback_note.update()
                except: pass
        except Exception as e:
            print(f"Error generating problem for rule {self.selected_rule.id} with kwargs {kwargs}: {e}")
            self.current_problem = {"question": "Error", "answer": 0}

        self.problem_text.value = to_lang_digits(self.current_problem["question"], self.lang)
        self.problem_text.scale = 1.0
        self.answer_input.value = ""
        self.answer_input.disabled = False
        self.feedback_text.value = ""
        self.check_button.visible = True
        self.next_button.visible = False

        # Update steps in Learn mode
        if self.mode == "Learn":
            self.steps_column.controls.clear()
            steps = self.selected_rule.get_steps(self.current_problem, self.lang)
            self.page.run_task(self.reveal_steps, steps)

        self.page.update()
        try:
            if self.answer_input.page:
                await self.answer_input.focus()
        except: pass

    async def reveal_steps(self, steps):
        self.steps_column.controls.clear()
        for step in steps:
            self.steps_column.controls.append(
                ft.Text(step, size=14, color=ft.Colors.GREY_400, opacity=0,
                        animate_opacity=ft.Animation(300))
            )
            self.steps_column.controls[-1].opacity = 1
            self.steps_column.update()
            await asyncio.sleep(0.6)

    async def handle_submit(self, e):
        if self.check_button.visible: await self.check_answer(e)
        else: await self.next_problem()

    async def check_answer(self, e):
        self.feedback_text.opacity = 0
        self.feedback_text.update()
        ui = LOCALIZED_UI[self.lang]
        if not self.answer_input.value:
            self.feedback_text.value = "Enter a number" if self.lang == 'en' else "یک عدد وارد کنید"
            self.feedback_text.color = ft.Colors.ORANGE_400
            self.feedback_text.opacity = 1
            self.feedback_text.update()
            return
        try: user_val = int(self.answer_input.value)
        except:
            self.feedback_text.value = "Enter a number" if self.lang == 'en' else "یک عدد وارد کنید"
            self.feedback_text.color = ft.Colors.ORANGE_400
            self.feedback_text.opacity = 1
            self.feedback_text.update()
            return

        self.total += 1
        level, state, mascot = self.get_beast_state()

        if user_val == self.current_problem["answer"]:
            self.score += 1
            self.streak += 1
            self.daily_solved_count += 1

            xp_gain = 10 + (self.streak * 5)
            self.total_xp += xp_gain
            self.xp_today += xp_gain

            if self.streak > self.best_streak:
                self.best_streak = self.streak

            # Record solve time
            solve_time = time.time() - self.problem_start_time
            self.solve_times.append(solve_time)

            self.feedback_text.value = f"{mascot} {ui['correct']}"
            self.feedback_text.color = COLOR_SUCCESS

            # Green pulse / Arena effect
            if hasattr(self, "arena_timer"):
                self.arena_timer.color = COLOR_SUCCESS
                self.arena_timer.update()

            self.trigger_success_animation(combo=self.streak)

            # Daily Challenge bonus
            if self.daily_solved_count == 20:
                self.total_xp += 150
                self.xp_today += 150
                # Could add a notification here

            # Streak Milestones
            if self.streak in [3, 5, 10]:
                milestone_text = ""
                if self.streak == 3: milestone_text = "🔥 Hot Streak" if self.lang == 'en' else "🔥 توالی داغ"
                elif self.streak == 5: milestone_text = "⚡ Beast Mode" if self.lang == 'en' else "⚡ وضعیت هیولا"
                elif self.streak == 10: milestone_text = "👑 Mental Math Monster" if self.lang == 'en' else "👑 غول محاسبات ذهنی"

                msg = ft.Container(
                    content=ft.Text(milestone_text, size=40, weight=ft.FontWeight.BOLD, color=COLOR_ACCENT),
                    opacity=0,
                    animate_opacity=ft.Animation(500),
                    scale=0.5,
                    animate_scale=ft.Animation(500, ft.AnimationCurve.BOUNCE_OUT)
                )
                self.page.overlay.append(msg)
                self.page.update()
                msg.opacity = 1
                msg.scale = 1
                msg.left = self.page.width/2 - 150
                msg.top = 100
                msg.update()

                async def remove_milestone(m):
                    await asyncio.sleep(2)
                    m.opacity = 0
                    m.update()
                    await asyncio.sleep(0.5)
                    if m in self.page.overlay: self.page.overlay.remove(m)
                    self.page.update()
                self.page.run_task(remove_milestone, msg)

        else:
            self.streak = 0
            ans_str = to_lang_digits(self.current_problem['answer'], self.lang)
            self.feedback_text.value = f"❌ {ui['wrong']} {ans_str}"
            self.feedback_text.color = ft.Colors.RED_400

            # Shake animation
            for _ in range(3):
                self.answer_input.offset = ft.Offset(0.02, 0)
                self.answer_input.update()
                await asyncio.sleep(0.05)
                self.answer_input.offset = ft.Offset(-0.02, 0)
                self.answer_input.update()
                await asyncio.sleep(0.05)
            self.answer_input.offset = ft.Offset(0, 0)
            self.answer_input.update()

            if hasattr(self, "arena_timer"):
                self.arena_timer.color = ft.Colors.RED_400
                self.arena_timer.update()

            # Reveal steps on wrong answer
            steps = self.selected_rule.get_steps(self.current_problem, self.lang)
            self.page.run_task(self.reveal_steps, steps)

        self.score_text.value = f"{ui['score']} {to_lang_digits(self.score, self.lang)}/{to_lang_digits(self.total, self.lang)}"
        self.streak_text.value = f"{ui['streak']} {to_lang_digits(self.streak, self.lang)}"
        self.save_state()
        self.answer_input.disabled = True
        self.check_button.visible = False
        self.next_button.visible = True
        self.feedback_text.opacity = 1
        self.page.update()

def main(page: ft.Page):
    MathBeast(page)

if __name__ == "__main__":
    ft.app(target=main)
