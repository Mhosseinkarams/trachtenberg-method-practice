import pytest
import asyncio
from unittest.mock import MagicMock, AsyncMock
import flet as ft
from app.main import FastMathApp

@pytest.mark.asyncio
async def test_app_initialization():
    # Mock Page
    page = MagicMock(spec=ft.Page)
    page.controls = []
    page.run_task = MagicMock()

    # Initialize App
    app = FastMathApp(page)

    assert page.title == "Fast Math Trainer"
    assert app.selected_rule is None
    # Check if header is added
    assert len(page.add.call_args[0][0].controls) > 0

@pytest.mark.asyncio
async def test_category_selection():
    page = MagicMock(spec=ft.Page)
    page.controls = []
    app = FastMathApp(page)

    # Manually trigger show_rule_selector
    app.show_rule_selector("Trachtenberg")

    # Verify main_content has controls
    assert len(app.main_content.controls) > 0
    # The first control should be the back button, the second the grid
    assert isinstance(app.main_content.controls[0], ft.TextButton)
    # In Flet 0.85.1, 'text' might not be an attribute. We just verify the type for now
    # or check the content if it's set.

@pytest.mark.asyncio
async def test_rule_selection_starts_timer():
    page = MagicMock(spec=ft.Page)
    page.controls = []
    app = FastMathApp(page)

    # Mock a Rule object
    rule = MagicMock()
    rule.method = "Trachtenberg"
    rule.name = "Test Rule"
    rule.generate_problem.return_value = {"question": "2+2", "answer": 4}

    app.select_rule(rule)

    assert app.selected_rule == rule
    assert app.timer_running is True
    assert app.timer_id == 1
    page.run_task.assert_any_call(app.update_timer, 1)

if __name__ == "__main__":
    pytest.main([__file__])
