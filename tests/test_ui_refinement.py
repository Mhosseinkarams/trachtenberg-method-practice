import pytest
from unittest.mock import MagicMock
import flet as ft
import sys
import os

# Add the project root to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import MathBeast

@pytest.mark.asyncio
async def test_language_toggle_preserves_state():
    page = MagicMock(spec=ft.Page)
    page.controls = []
    page.client_storage = MagicMock()
    page.client_storage.get.return_value = None

    app = MathBeast(page)
    app.lang = 'en' # Set to en first so toggle goes to fa

    # Select a rule and start Practice
    rule = MagicMock()
    rule.id = 'tracht-11'
    rule.get_name.return_value = "Test Rule"
    rule.category = "Multiplication"
    rule.generate_problem.return_value = {"question": "11 x 100", "answer": 1100, "num": 100}
    rule.get_steps.return_value = ["Step 1"]

    app.select_rule(rule)
    app.start_session("Practice")
    await app.next_problem()

    assert app.mode == "Practice"
    initial_problem = app.current_problem

    # Toggle language
    app.toggle_language(None)

    assert app.mode == "Practice"
    assert app.selected_rule == rule
    assert app.current_problem == initial_problem
    # In Persian it should be translated
    assert app.problem_text.value == "۱۱ x ۱۰۰"

if __name__ == "__main__":
    pytest.main([__file__])
