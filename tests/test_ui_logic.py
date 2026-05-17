import sys
import os
import asyncio
import pytest
from unittest.mock import MagicMock, AsyncMock

# Add the app directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))

import flet as ft
from main import FastMathApp
from math_logic import rules

class MockPage:
    def __init__(self):
        self.title = ""
        self.theme_mode = None
        self.padding = 0
        self.bgcolor = ""
        self.controls = []
        self.add = MagicMock()
        self.update = MagicMock()
        self.window_close = MagicMock()
        self.session_id = "test"
        self.pubsub = MagicMock()

@pytest.mark.asyncio
async def test_app_initialization():
    page = MockPage()
    app = FastMathApp(page)
    # Mock focus to avoid "Control must be added to page" error
    ft.TextField.focus = AsyncMock()

    await app.initialize()

    assert page.title == "Fast Math Trainer"
    assert app.selected_rule is None
    assert len(app.main_content.controls) > 0

@pytest.mark.asyncio
async def test_rule_selection():
    page = MockPage()
    app = FastMathApp(page)
    ft.TextField.focus = AsyncMock()

    await app.initialize()

    rule = rules[0]
    await app.select_rule(rule)

    assert app.selected_rule == rule
    assert app.score == 0
    assert app.total == 0
    assert app.problem_text.value != ""

@pytest.mark.asyncio
async def test_check_answer_correct():
    page = MockPage()
    app = FastMathApp(page)
    ft.TextField.focus = AsyncMock()

    await app.initialize()

    rule = rules[0]
    await app.select_rule(rule)

    app.current_problem = {"question": "11 x 100", "answer": 1100}
    app.problem_text.value = "11 x 100"

    app.answer_input.value = "1100"
    await app.check_answer(None)

    assert app.score == 1
    assert app.total == 1
    assert "Correct" in app.feedback_text.value
    assert app.submit_button.text == "Next Problem"

@pytest.mark.asyncio
async def test_check_answer_wrong():
    page = MockPage()
    app = FastMathApp(page)
    ft.TextField.focus = AsyncMock()

    await app.initialize()

    rule = rules[0]
    await app.select_rule(rule)

    app.current_problem = {"question": "11 x 100", "answer": 1100}
    app.problem_text.value = "11 x 100"

    app.answer_input.value = "1101"
    await app.check_answer(None)

    assert app.score == 0
    assert app.total == 1
    assert "Wrong" in app.feedback_text.value
    assert app.submit_button.text == "Next Problem"
