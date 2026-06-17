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
<<<<<<< Updated upstream
    # Check if root container is added
    assert isinstance(page.add.call_args[0][0], ft.Container)
=======
    # Check if header is added
    assert len(page.add.call_args[0][0].controls) > 0
>>>>>>> Stashed changes

@pytest.mark.asyncio
async def test_category_selection():
    page = MagicMock(spec=ft.Page)
    page.controls = []
    app = FastMathApp(page)

    # Manually trigger show_rule_selector with new category
    app.show_rule_selector("Multiplication")

<<<<<<< Updated upstream
    # Verify main_content has content
    assert app.main_content.content is not None
    # The first control in the view should be the back button (wrapped in a Row)
    assert isinstance(app.main_content.content.controls[0].controls[0], ft.TextButton)
=======
    # Verify main_content has controls
    assert len(app.main_content.controls) > 0
    # The first control should be the back button
    assert isinstance(app.main_content.controls[0], ft.TextButton)
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
    assert app.main_content.content is not None
    # Find mode selection text (localized)
    found = False
    target_prefix = LOCALIZED_UI['fa']['target']
    for control in app.main_content.content.controls:
=======
    assert len(app.main_content.controls) > 0
    # Find mode selection text (localized)
    found = False
    target_prefix = LOCALIZED_UI['fa']['target']
    for control in app.main_content.controls:
>>>>>>> Stashed changes
        if isinstance(control, ft.Text) and target_prefix in control.value:
            found = True
            break
    assert found

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
