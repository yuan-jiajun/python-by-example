# 💰 Project 02: Expense Tracker

## Difficulty: 🟡 Intermediate

## Description
Build a command-line expense tracker that allows users to add, view, and analyze
their expenses. Data is saved to a JSON file so expenses persist between sessions.

## Requirements

1. Add new expenses with a description, amount, and category
2. View all expenses in a formatted table
3. Filter expenses by category
4. Show a summary with total spending and spending per category
5. Save and load expenses from a JSON file
6. Delete an expense by its ID

## Concepts You'll Practice

- Dictionaries and Lists
- File I/O (JSON)
- Functions with multiple parameters
- String formatting
- `datetime` module
- Data filtering and aggregation

## Example Output

```
💰 EXPENSE TRACKER
==================

1. Add Expense
2. View All Expenses
3. View by Category
4. Summary
5. Delete Expense
6. Exit

Choose an option: 1

Enter description: Coffee
Enter amount: 4.50
Enter category (food/transport/entertainment/bills/other): food
✅ Expense added successfully!

Choose an option: 4

📊 EXPENSE SUMMARY
Total Expenses: $127.50
  🍔 Food:          $45.00 (35.3%)
  🚗 Transport:     $32.50 (25.5%)
  🎬 Entertainment: $25.00 (19.6%)
  📄 Bills:         $25.00 (19.6%)
```

## How to Run

```bash
cd projects/02_expense_tracker
python solution.py
```

## Bonus Challenges

- [ ] Add monthly budget limits with warnings
- [ ] Export expenses to CSV
- [ ] Add date range filtering
