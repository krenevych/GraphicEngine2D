import os
import pytest


@pytest.fixture(autouse=True)
def change_test_dir(monkeypatch):
    """
    Змінює поточну директорію на tests/ для всіх тестів.
    Це дозволяє коректно вирішувати відносні шляхи, наприклад:
        "expected/Figure_1.png"  ->  tests/expected/Figure_1.png
    """
    monkeypatch.chdir(os.path.dirname(__file__))
