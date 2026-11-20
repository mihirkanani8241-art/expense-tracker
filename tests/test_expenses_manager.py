
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch

from expense_manager import (
    add_expense,
    list_expenses,
    delete_expense,
    get_summary,
    get_monthly_summary,
    get_category_summary
)


class TestExpenseManager(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.csv_path = Path(self.temp_dir.name) / "expenses.csv"

        self.file_patcher = patch("storage.FILE_NAME", self.csv_path)
        self.file_patcher.start()

    def tearDown(self):
        self.file_patcher.stop()
        self.temp_dir.cleanup()

    def test_add_expense(self):
        expense = add_expense(
            "2026-11-20", "Lunch", "Food", 150
        )
        self.assertEqual(expense["id"], "1")
        self.assertEqual(len(list_expenses()), 1)

    def test_list_expenses(self):
        add_expense("2026-11-20", "Lunch", "Food", 150)
        self.assertEqual(len(list_expenses()), 1)

    def test_delete_expense(self):
        add_expense("2026-11-20", "Lunch", "Food", 150)
        self.assertTrue(delete_expense(1))
        self.assertEqual(len(list_expenses()), 0)

    def test_delete_missing_expense(self):
        self.assertFalse(delete_expense(99))

    def test_total_summary(self):
        add_expense("2026-11-20", "Lunch", "Food", 150)
        add_expense("2026-11-20", "Bus", "Travel", 30)
        self.assertEqual(get_summary(), 180)

    def test_monthly_summary(self):
        add_expense("2026-11-20", "Lunch", "Food", 150)
        add_expense("2026-12-01", "Bus", "Travel", 30)
        self.assertEqual(get_monthly_summary("2026-11"), 150)

    def test_category_summary(self):
        add_expense("2026-11-20", "Lunch", "Food", 150)
        add_expense("2026-11-21", "Dinner", "Food", 100)
        add_expense("2026-11-20", "Bus", "Travel", 30)

        summary = get_category_summary()

        self.assertEqual(summary["Food"], 250)
        self.assertEqual(summary["Travel"], 30)


if __name__ == "__main__":
    unittest.main()
