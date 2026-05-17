import flet as ft
from math_logic import rules, rules_by_method

class FastMathApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Fast Math Trainer"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.padding = 20
        self.page.bgcolor = ft.Colors.GREY_50

        self.selected_rule = None
        self.current_problem = None
        self.current_problem_answered = False
        self.score = 0
        self.total = 0

        self.setup_ui()

    def setup_ui(self):
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

    def show_rule_selector(self, update=True):
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
        self.show_practice_area()

    def show_practice_area(self):
        self.main_content.controls.clear()

        back_button = ft.TextButton(
            "Back to methods",
            icon=ft.Icons.ARROW_BACK,
            on_click=lambda _: self.show_rule_selector()
        )

        self.problem_text = ft.Text("", size=48, weight=ft.FontWeight.BOLD)
        self.answer_input = ft.TextField(
            label="Enter answer",
            text_align=ft.TextAlign.CENTER,
            on_submit=self.check_answer,
            keyboard_type=ft.KeyboardType.NUMBER
        )
        self.feedback_text = ft.Text("", size=18, weight=ft.FontWeight.BOLD)
        self.score_text = ft.Text(f"Score: 0/0", size=16)
        self.submit_button = ft.ElevatedButton("Check Answer", on_click=self.check_answer, width=400, bgcolor=ft.Colors.INDIGO_600, color=ft.Colors.WHITE)

        practice_card = ft.Container(
            content=ft.Column([
                ft.Row([ft.Text(self.selected_rule.name, weight=ft.FontWeight.BOLD), self.score_text], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Divider(),
                ft.Column([
                    self.problem_text,
                    ft.Text("= ?", size=20, color=ft.Colors.GREY_400),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                self.answer_input,
                self.submit_button,
                self.feedback_text,
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
            padding=30,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.GREY_300)
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
                ft.Column([practice_card], col={"lg": 6}),
                ft.Column([theory_card], col={"lg": 6})
            ])
        )

        self.next_problem()

    def next_problem(self, update=True):
        self.current_problem = self.selected_rule.generate_problem()
        self.problem_text.value = self.current_problem["question"]
        self.answer_input.value = ""
        self.feedback_text.value = ""
        self.current_problem_answered = False
        self.submit_button.text = "Check Answer"
        self.submit_button.bgcolor = ft.Colors.INDIGO_600
        self.answer_input.focus()
        if update:
            self.page.update()

    def check_answer(self, e):
        if self.current_problem_answered:
            self.next_problem()
            return

        if not self.answer_input.value:
            return

        try:
            user_val = int(self.answer_input.value)
        except ValueError:
            return

        self.current_problem_answered = True
        self.total += 1
        if user_val == self.current_problem["answer"]:
            self.score += 1
            self.feedback_text.value = "Correct!"
            self.feedback_text.color = ft.Colors.GREEN_600
            self.submit_button.bgcolor = ft.Colors.GREEN_600
        else:
            self.feedback_text.value = f"Wrong. The answer was {self.current_problem['answer']}"
            self.feedback_text.color = ft.Colors.RED_600
            self.submit_button.bgcolor = ft.Colors.ORANGE_600

        self.submit_button.text = "Next Problem"
        self.score_text.value = f"Score: {self.score}/{self.total}"
        self.page.update()

def main(page: ft.Page):
    FastMathApp(page)

if __name__ == "__main__":
    ft.app(target=main)
