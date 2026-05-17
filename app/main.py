import flet as ft
import time
import asyncio
try:
    from math_logic import rules, rules_by_method
except ImportError:
    from app.math_logic import rules, rules_by_method

class FastMathApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Fast Math Trainer"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.padding = 20
        self.page.bgcolor = ft.Colors.GREY_50

        self.selected_rule = None
        self.current_problem = None
        self.score = 0
        self.total = 0
        self.streak = 0
        self.start_time = None
        self.timer_running = False

        self.setup_ui()

    def setup_ui(self, update: bool = True):
        self.header = ft.Container(
            content=ft.Column([
                ft.Text("Fast Math Trainer", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900),
                ft.Text("Master Rapid Calculation", size=16, color=ft.Colors.GREY_600),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            margin=ft.Margin.only(bottom=20),
            alignment=ft.Alignment.CENTER
        )

        self.main_content = ft.Column(expand=True)
        self.show_rule_selector(update=False)

        self.page.add(
            ft.Column([
                self.header,
                self.main_content,
                ft.Divider(),
                ft.Text("© 2024 Fast Math Trainer. Built with Flet.", size=12, color=ft.Colors.GREY_400, text_align=ft.TextAlign.CENTER)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True)
        )
        if update:
            self.page.update()

    def show_rule_selector(self, update: bool = True):
        self.main_content.controls.clear()

        sections = [
            ("Trachtenberg System", rules_by_method["Trachtenberg"]),
            ("Vedic Mathematics", rules_by_method["Vedic"])
        ]

        grid = ft.Column(spacing=20)

        for title, rule_list in sections:
            grid.controls.append(ft.Text(title, size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_800))

            rule_grid = ft.ResponsiveRow(spacing=10)
            for rule in rule_list:
                rule_grid.controls.append(
                    ft.Container(
                        content=ft.Column([
                            ft.Text(rule.name, weight=ft.FontWeight.BOLD, size=18),
                            ft.Text(rule.description, size=14, color=ft.Colors.GREY_600),
                        ]),
                        padding=20,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=10,
                        border=ft.Border.all(1, ft.Colors.GREY_200),
                        on_click=lambda e, r=rule: self.select_rule(r),
                        col={"sm": 12, "md": 6, "lg": 4},
                        ink=True
                    )
                )
            grid.controls.append(rule_grid)

        self.main_content.controls.append(grid)
        if update:
            self.page.update()

    def select_rule(self, rule):
        self.selected_rule = rule
        self.score = 0
        self.total = 0
        self.streak = 0
        self.start_time = time.time()
        # Initialize UI first to ensure timer_text exists before starting the timer task
        self.show_practice_area()
        if not self.timer_running:
            self.timer_running = True
            self.page.run_task(self.update_timer)

    async def update_timer(self):
        while self.timer_running:
            if self.start_time:
                elapsed = int(time.time() - self.start_time)
                mins, secs = divmod(elapsed, 60)
                self.timer_text.value = f"Time: {mins:02d}:{secs:02d}"
                self.timer_text.update()
            await asyncio.sleep(1)

    def show_practice_area(self, update: bool = True):
        self.main_content.controls.clear()

        def go_back(e):
            self.timer_running = False
            self.show_rule_selector()

        back_button = ft.TextButton(
            "Back to methods",
            icon=ft.Icons.ARROW_BACK,
            on_click=go_back
        )

        self.problem_text = ft.Text("", size=48, weight=ft.FontWeight.BOLD)
        self.answer_input = ft.TextField(
            label="Enter answer",
            text_align=ft.TextAlign.CENTER,
            on_submit=self.handle_submit,
            keyboard_type=ft.KeyboardType.NUMBER,
            autofocus=True
        )
        self.feedback_text = ft.Text("", size=18, weight=ft.FontWeight.BOLD)
        self.score_text = ft.Text(f"Score: 0/0", size=16)
        self.streak_text = ft.Text(f"Streak: 0", size=16, color=ft.Colors.ORANGE_800, weight=ft.FontWeight.BOLD)
        self.timer_text = ft.Text(f"Time: 00:00", size=16)
        self.check_button = ft.ElevatedButton(text="Check Answer", on_click=self.check_answer, width=400, bgcolor=ft.Colors.INDIGO_600, color=ft.Colors.WHITE)
        self.next_button = ft.ElevatedButton(text="Next Problem", on_click=self.next_problem, width=400, bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE, visible=False)

        self.practice_card = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Column([
                        ft.Text(self.selected_rule.name, weight=ft.FontWeight.BOLD),
                        self.timer_text
                    ]),
                    ft.Column([
                        self.score_text,
                        self.streak_text
                    ], horizontal_alignment=ft.CrossAxisAlignment.END)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Divider(),
                ft.Column([
                    self.problem_text,
                    ft.Text("= ?", size=20, color=ft.Colors.GREY_400),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                self.answer_input,
                self.check_button,
                self.next_button,
                self.feedback_text,
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
            padding=30,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.GREY_300),
            animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT)
        )

        theory_card = ft.Container(
            content=ft.Column([
                ft.Text("Theory", size=24, weight=ft.FontWeight.BOLD),
                ft.Text(self.selected_rule.explanation, size=16),
                ft.Text("Example", size=20, weight=ft.FontWeight.BOLD),
                ft.Container(
                    content=ft.Text(self.selected_rule.example, font_family="monospace"),
                    padding=10,
                    bgcolor=ft.Colors.GREY_100,
                    border_radius=5
                )
            ], spacing=15),
            padding=30,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            border=ft.Border.all(1, ft.Colors.GREY_200)
        )

        self.main_content.controls.append(back_button)
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
        self.current_problem = self.selected_rule.generate_problem()
        self.problem_text.value = self.current_problem["question"]
        self.answer_input.value = ""
        self.answer_input.disabled = False
        self.feedback_text.value = ""
        self.check_button.visible = True
        self.next_button.visible = False
        self.practice_card.bgcolor = ft.Colors.WHITE
        self.page.update()
        # In Flet 0.85.1, TextField.focus() is a coroutine and must be awaited
        await self.answer_input.focus()

    async def handle_submit(self, e):
        if self.check_button.visible:
            await self.check_answer(e)
        else:
            await self.next_problem()

    async def check_answer(self, e):
        if not self.answer_input.value:
            return

        try:
            user_val = int(self.answer_input.value)
        except ValueError:
            return

        self.total += 1
        if user_val == self.current_problem["answer"]:
            self.score += 1
            self.streak += 1
            self.feedback_text.value = "Correct!"
            self.feedback_text.color = ft.Colors.GREEN_600
            self.practice_card.bgcolor = ft.Colors.GREEN_50
        else:
            self.streak = 0
            self.feedback_text.value = f"Wrong. The answer was {self.current_problem['answer']}"
            self.feedback_text.color = ft.Colors.RED_600
            self.practice_card.bgcolor = ft.Colors.RED_50

        self.score_text.value = f"Score: {self.score}/{self.total}"
        self.streak_text.value = f"Streak: {self.streak}"
        self.answer_input.disabled = True
        self.check_button.visible = False
        self.next_button.visible = True
        self.page.update()
        # In Flet 0.85.1, Button.focus() is a coroutine and must be awaited
        await self.next_button.focus()

def main(page: ft.Page):
    FastMathApp(page)

if __name__ == "__main__":
    ft.app(target=main)
