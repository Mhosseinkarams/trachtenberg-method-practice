import pytest
import asyncio
from unittest.mock import MagicMock, AsyncMock
import flet as ft
from app.main import FastMathApp, LOCALIZED_UI

@pytest.mark.asyncio
async def test_app_initialization():
    # Mock Page
    page = MagicMock(spec=ft.Page)
    page.controls = []
    page.run_task = MagicMock()

    # Initialize App
    app = FastMathApp(page)

    assert page.title == LOCALIZED_UI['fa']['title']
    assert app.selected_rule is None
    # Check if header is added
    assert len(page.add.call_args[0][0].controls) > 0

@pytest.mark.asyncio
async def test_category_selection():
    page = MagicMock(spec=ft.Page)
    page.controls = []
    app = FastMathApp(page)

    # Manually trigger show_rule_selector with new category
    app.show_rule_selector("Multiplication")

    # Verify main_content has controls
    assert len(app.main_content.controls) > 0
    # The view might be wrapped in a Column due to caching optimization
    content = app.main_content.controls[0]
    if isinstance(content, ft.Column):
        content = content.controls[0]
    # The first control should be the back button
    assert isinstance(content, ft.TextButton)

@pytest.mark.asyncio
async def test_rule_selection_shows_modes():
    page = MagicMock(spec=ft.Page)
    page.controls = []
    app = FastMathApp(page)

    rule = MagicMock()
    rule.get_name.return_value = "Test Rule"
    rule.category = "Multiplication"

    app.select_rule(rule)

    assert app.selected_rule == rule
    # Should show mode selection cards
    assert len(app.main_content.controls) > 0
    # Find mode selection text (localized)
    found = False
    target_prefix = LOCALIZED_UI['fa']['target']

    def search_controls(controls):
        for control in controls:
            if isinstance(control, ft.Text) and control.value and target_prefix in control.value:
                return True
            if hasattr(control, "controls") and search_controls(control.controls):
                return True
        return False

    assert search_controls(app.main_content.controls)

@pytest.mark.asyncio
async def test_start_session_starts_timer():
    page = MagicMock(spec=ft.Page)
    page.controls = []
    app = FastMathApp(page)

    rule = MagicMock()
    rule.get_name.return_value = "Test Rule"
    rule.category = "Multiplication"
    rule.generate_problem.return_value = {"question": "2+2", "answer": 4}
    rule.get_steps.return_value = ["Step 1"]
    app.selected_rule = rule

    app.start_session("Practice")

    assert app.mode == "Practice"
    assert app.timer_running is True
    assert app.timer_id == 1
    page.run_task.assert_any_call(app.update_timer, 1)

if __name__ == "__main__":
    pytest.main([__file__])
