# Expense Tracker CLI

A command-line application built with Python to track and manage personal expenses.

## Features

- Add expenses with date, description, category and amount
- List all recorded expenses
- Delete expenses using their ID
- Calculate total expenses
- Calculate monthly expenses
- View category-wise expense summaries
- Store expense data in a CSV file
- Validate expense inputs
- Automated unit tests

## Requirements

- Python 3.8 or later

## Installation

Clone the repository:

```bash
git clone https://github.com/mihirkanani8241-art/expense-tracker.git
cd expense-tracker
```

## Usage

### Add an expense

```bash
python main.py add --date 2026-11-20 --description Lunch --category Food --amount 150
```

### List expenses

```bash
python main.py list
```

### Delete an expense

```bash
python main.py delete 1
```

### Total expense summary

```bash
python main.py summary
```

### Monthly expense summary

```bash
python main.py summary --month 2026-11
```

### Category-wise summary

```bash
python main.py categories
```

### Help

```bash
python main.py --help
```

## Running Tests

```bash
python -m unittest discover -s tests -v
```

## Project Structure

```text
expense-tracker/
├── main.py
├── expense_manager.py
├── storage.py
├── expenses.csv
├── README.md
├── .gitignore
└── tests/
    └── test_expenses_manager.py
```

## Technologies

- Python
- CSV
- argparse
- unittest

## Project URL

https://roadmap.sh/projects/expense-tracker

## Author

Mihir Kanani

GitHub: https://github.com/mihirkanani8241-art