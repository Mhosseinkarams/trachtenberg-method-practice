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
        self.timer_id = 0
        self.mode = "Learn" # Default mode

        self.setup_ui()

    def setup_ui(self, update: bool = True):
        self.page.scroll = ft.ScrollMode.AUTO
        self.header = ft.Container(
            content=ft.Column([
                ft.Text("Fast Math Trainer", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900),
                ft.Text("Master Rapid Calculation", size=16, color=ft.Colors.GREY_600),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            margin=ft.Margin.only(bottom=20),
            alignment=ft.Alignment.CENTER
        )

        self.main_content = ft.Column()
        self.show_categories(update=False)

        self.page.add(
            ft.Column([
                self.header,
                self.main_content,
                ft.Divider(),
                ft.Text("© 2024 Fast Math Trainer. Built with Flet.", size=12, color=ft.Colors.GREY_400, text_align=ft.TextAlign.CENTER)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )
        if update:
            self.page.update()

    def show_categories(self, update: bool = True):
        self.main_content.controls.clear()

        categories = [
            ("Trachtenberg System", "Advanced mental multiplication and addition.", ft.Colors.BLUE_700, ft.Icons.GRID_VIEW),
            ("Vedic Mathematics", "Ancient Indian techniques for rapid calculation.", ft.Colors.ORANGE_700, ft.Icons.PSYCHOLOGY)
        ]

        category_grid = ft.ResponsiveRow(spacing=20)
        for name, desc, color, icon in categories:
            method_key = "Trachtenberg" if "Trachtenberg" in name else "Vedic"
            category_grid.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Icon(icon, size=40, color=color),
                        ft.Text(name, size=24, weight=ft.FontWeight.BOLD),
                        ft.Text(desc, size=16, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=40,
                    bgcolor=ft.Colors.WHITE,
                    border_radius=15,
                    border=ft.Border.all(1, ft.Colors.GREY_200),
                    on_click=lambda e, m=method_key: self.show_rule_selector(m),
                    col={"sm": 12, "md": 6},
                    ink=True
                )
            )

        self.main_content.controls.append(category_grid)
        if update:
            self.page.update()

    def show_rule_selector(self, method: str, update: bool = True):
        self.main_content.controls.clear()

        back_button = ft.TextButton(
            "Back to Categories",
            icon=ft.Icons.ARROW_BACK,
            on_click=lambda _: self.show_categories()
        )

        rule_list = rules_by_method[method]

        grid = ft.Column(spacing=20)
        grid.controls.append(ft.Text(f"{method} Methods", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_800))

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

        self.main_content.controls.append(back_button)
        self.main_content.controls.append(grid)
        if update:
            self.page.update()

    def select_rule(self, rule):
        self.selected_rule = rule
        self.show_mode_selection()

    def show_mode_selection(self, update: bool = True):
        self.main_content.controls.clear()

        back_button = ft.TextButton(
            "Back to methods",
            icon=ft.Icons.ARROW_BACK,
            on_click=lambda _: self.show_rule_selector(self.selected_rule.method)
        )

        cards = ft.ResponsiveRow([
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.SCHOOL, size=40, color=ft.Colors.BLUE_600),
                    ft.Text("Learn", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text("Study the theory and see examples.", size=16, color=ft.Colors.GREY_600),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=40, bgcolor=ft.Colors.WHITE, border_radius=15, col={"sm": 12, "md": 6},
                on_click=lambda _: self.start_session("Learn"), ink=True
            ),
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.TIMER, size=40, color=ft.Colors.ORANGE_600),
                    ft.Text("Practice", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text("Test your speed and accuracy.", size=16, color=ft.Colors.GREY_600),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=40, bgcolor=ft.Colors.WHITE, border_radius=15, col={"sm": 12, "md": 6},
                on_click=lambda _: self.start_session("Practice"), ink=True
            )
        ], spacing=20)

        self.main_content.controls.append(back_button)
        self.main_content.controls.append(ft.Text(f"Target: {self.selected_rule.name}", size=20, weight=ft.FontWeight.BOLD))
        self.main_content.controls.append(cards)
        if update:
            self.page.update()

    def start_session(self, mode):
        self.mode = mode
        self.score = 0
        self.total = 0
        self.streak = 0
        self.start_time = time.time()

        # Increment timer_id to invalidate any previous timer tasks
        self.timer_id += 1
        self.timer_running = True

        # Initialize UI first to ensure timer_text exists before starting the timer task
        self.show_practice_area()
        self.page.run_task(self.update_timer, self.timer_id)

    async def update_timer(self, tid):
        while self.timer_running and self.timer_id == tid:
            if self.start_time and hasattr(self, "timer_text"):
                try:
                    elapsed = int(time.time() - self.start_time)
                    mins, secs = divmod(elapsed, 60)
                    self.timer_text.value = f"Time: {mins:02d}:{secs:02d}"
                    # Only update if the control is still part of the page to avoid errors
                    if self.timer_text.page:
                        self.timer_text.update()
                    else:
                        # Fallback to page update if control is not yet attached
                        self.page.update()
                except Exception:
                    # Handle cases where timer_text might be briefly unavailable during transitions
                    pass
            await asyncio.sleep(1)

    def show_practice_area(self, update: bool = True):
        self.main_content.controls.clear()

        config_panel = ft.Column(visible=False)
        if self.mode == "Practice" and self.selected_rule.id in ['tracht-addition', 'vedic-complementary-addition', 'vedic-subtraction-base']:
            self.num_operands_slider = ft.Slider(min=2, max=5, divisions=3, label="{value} numbers", value=2)
            self.num_digits_dropdown = ft.Dropdown(
                label="Digits per number",
                options=[
                    ft.dropdown.Option("0", "Random"),
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
                ft.Text("Customization Panel", weight=ft.FontWeight.BOLD),
                ft.Row([
                    ft.Column([ft.Text("Count"), self.num_operands_slider]) if self.selected_rule.id != 'vedic-subtraction-base' else ft.Column(),
                    self.num_digits_dropdown
                ], alignment=ft.MainAxisAlignment.START),
                ft.ElevatedButton("Apply & Restart", on_click=lambda _: self.page.run_task(self.next_problem)),
                ft.Divider()
            ])
            config_panel.visible = True

        def go_back(e):
            self.timer_running = False
            self.show_mode_selection()

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
        self.check_button = ft.ElevatedButton(content=ft.Text("Check Answer"), on_click=self.check_answer, width=400, bgcolor=ft.Colors.INDIGO_600, color=ft.Colors.WHITE)
        self.next_button = ft.ElevatedButton(content=ft.Text("Next Problem"), on_click=self.next_problem, width=400, bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE, visible=False)

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
                ft.Text("Theory & Shortcuts", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_700),
                ft.Text(self.selected_rule.explanation, size=16),
                ft.Text("Example", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_800),
                ft.Container(
                    content=ft.Text(self.selected_rule.example, font_family="monospace", size=14),
                    padding=15,
                    bgcolor=ft.Colors.GREY_100,
                    border_radius=10,
                    border=ft.Border.all(1, ft.Colors.GREY_300)
                )
            ], spacing=15),
            padding=30,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            border=ft.Border.all(1, ft.Colors.GREY_200)
        )

        self.main_content.controls.append(back_button)
        if config_panel.visible:
            self.main_content.controls.append(config_panel)

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
        except Exception as ex:
            print(f"Error generating problem: {ex}")
            self.current_problem = {"question": "Error", "answer": 0}

        self.problem_text.value = self.current_problem["question"]
        self.answer_input.value = ""
        self.answer_input.disabled = False
        self.feedback_text.value = ""
        self.check_button.visible = True
        self.next_button.visible = False
        self.practice_card.bgcolor = ft.Colors.WHITE
        # Granular update of the practice card instead of the whole page
        self.practice_card.update()
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
        # Granular update of the practice card instead of the whole page
        self.practice_card.update()
        # In Flet 0.85.1, Button.focus() is a coroutine and must be awaited
        await self.next_button.focus()

def main(page: ft.Page):
    FastMathApp(page)

if __name__ == "__main__":
    ft.app(target=main)
