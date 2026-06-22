import asyncio
from unittest.mock import MagicMock
import flet as ft
import sys
import os
import json
from datetime import datetime

# Add the project root to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app.main import MathBeast

@pytest.mark.asyncio
async def test_persistence():
    page = MagicMock(spec=ft.Page)
    page.client_storage = MagicMock()
    page.controls = []

    # Mock storage data
    test_data = {
        "total_xp": 500,
        "xp_today": 50,
        "daily_solved_count": 5,
        "best_streak": 10,
        "solve_times": [5.5, 4.2],
        "last_solve_date": datetime.now().strftime("%Y-%m-%d")
    }
    page.client_storage.get.return_value = json.dumps(test_data)

    app = MathBeast(page)

    print("Verifying loaded data...")
    assert app.total_xp == 500
    assert app.xp_today == 50
    assert app.daily_solved_count == 5
    assert app.best_streak == 10
    assert app.solve_times == [5.5, 4.2]
    print("Loaded data verified.")

    # Test saving
    app.total_xp += 100
    app.save_state()

    called_args = page.client_storage.set.call_args[0]
    assert called_args[0] == "mathbeast_state"
    saved_data = json.loads(called_args[1])
    assert saved_data["total_xp"] == 600
    print("Saved data verified.")

    # Test daily reset
    app.last_solve_date = "2000-01-01"
    app.check_daily_reset()
    assert app.xp_today == 0
    assert app.daily_solved_count == 0
    assert app.last_solve_date == datetime.now().strftime("%Y-%m-%d")
    print("Daily reset verified.")

if __name__ == "__main__":
    asyncio.run(test_persistence())
