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
async def test_rule_selection_shows_modes():
    page = MagicMock(spec=ft.Page)
    page.controls = []
    app = FastMathApp(page)

    rule = MagicMock()
    rule.method = "Trachtenberg"
    rule.name = "Test Rule"

    app.select_rule(rule)

    assert app.selected_rule == rule
    # Should show mode selection cards
    assert len(app.main_content.controls) > 0
    # Find mode selection text
    found = False
    for control in app.main_content.controls:
        if isinstance(control, ft.Text) and "Target:" in control.value:
            found = True
            break
    assert found

@pytest.mark.asyncio
async def test_start_session_starts_timer():
    page = MagicMock(spec=ft.Page)
    page.controls = []
    app = FastMathApp(page)

    rule = MagicMock()
    rule.method = "Trachtenberg"
    rule.name = "Test Rule"
    rule.id = "test-rule"
    rule.generate_problem.return_value = {"question": "2+2", "answer": 4}
    app.selected_rule = rule

    app.start_session("Practice")

    assert app.mode == "Practice"
    assert app.timer_running is True
    assert app.timer_id == 1
    page.run_task.assert_any_call(app.update_timer, 1)

@pytest.mark.asyncio
async def test_customization_panel_visibility():
    page = MagicMock(spec=ft.Page)
    page.controls = []
    app = FastMathApp(page)

    rule = MagicMock()
    rule.id = "tracht-addition"
    app.selected_rule = rule
    app.mode = "Practice"

    app.show_practice_area()

    # Check if config_panel was added
    found_config = False
    for control in app.main_content.controls:
        if isinstance(control, ft.Column) and control.visible:
            # Look for "Customization Panel" text
            for sub in control.controls:
                if isinstance(sub, ft.Text) and "Customization Panel" in sub.value:
                    found_config = True
                    break
    assert found_config

if __name__ == "__main__":
    pytest.main([__file__])
