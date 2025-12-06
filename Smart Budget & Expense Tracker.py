"""
SMART BUDGET & EXPENSE TRACKER
Author: <Ken Benitez, Melrhenzon Flores, Hans Rodis, Jacob Robinion, Enoch Camayang, Anoujh Escolta> <DREAM TEAM>
Course: COMPUTER PROGRAMMING
Description:
    A program that allows the user to record expenses,
    categorize them, and view summary reports. Includes full usage of:
    - Input/Output, Escape Sequences, Placeholders
    - Arithmetic, Assignment, Bitwise Operators
    - String Handling, Typecasting
    - Math + String Functions
    - Selection Structures (if, elif, else)
    - Loops, Break, Continue
    - Lists, Tuples, Sets
"""

# ============================
# Lesson 1: OUTPUT, INPUT, ESCAPE SEQUENCES, PLACEHOLDERS
# ============================

print("\n==============================")
print("   SMART BUDGET TRACKER")
print("==============================\n")

# ============================
# Lesson 8: TUPLE (Fixed categories)
# ============================

CATEGORIES = ("Food", "Transport", "Bills", "Shopping", "School", "Others")

# ============================
# Storage for expenses (Lesson 8: LIST)
# Each item stored as: {"amount": float, "category": str}
# ============================

expenses = []
used_categories = set()  # (Lesson 8: SET → to track unique categories used)


# ----------------------------
# Function: Add Expense
# Lessons Used:
# Input, Typecasting, Conditionals, String Handling, Arithmetic, Assignment,
# Bitwise Operator example, String Functions, Lists, Sets
# ----------------------------

def add_expense():
    print("\n--- ADD NEW EXPENSE ---")

    # Input with typecasting (Lesson 4)
    try:
        amount = float(input("Enter amount: ₱"))
    except ValueError:
        print("Invalid amount! Please enter numbers only.")
        return

    # String handling (Lesson 3)
    print("\nAvailable Categories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"[{i}] {cat}")

    try:
        cat_choice = int(input("\nChoose category number: "))
        if not (1 <= cat_choice <= len(CATEGORIES)):
            print("Invalid category.")
            return
    except ValueError:
        print("Invalid input.")
        return

    category = CATEGORIES[cat_choice - 1]
    used_categories.add(category)  # track categories used

    # Bitwise example: check if amount is even or odd (Lesson 2)
    if int(amount) & 1:
        even_odd = "Odd Amount"
    else:
        even_odd = "Even Amount"

    expenses.append({"amount": amount, "category": category})

    print(f"\n👍 Successfully added ₱{amount:.2f} under {category}. ({even_odd})")


# ----------------------------
# Function: View All Expenses
# Lessons Used: Loops, String Formatting, Escape Sequences
# ----------------------------

def view_expenses():
    print("\n--- ALL RECORDED EXPENSES ---\n")

    if not expenses:
        print("No expenses found.\n")
        return

    for i, item in enumerate(expenses, 1):
        print(f"{i}. ₱{item['amount']:.2f}  -  {item['category']}")


# ----------------------------
# Function: Summary Report
# Lessons Used: Predefined Math Functions, Loops, Conditionals, String Handling
# ----------------------------

def summary_report():
    print("\n--- SUMMARY REPORT ---\n")

    if not expenses:
        print("No data available for report.\n")
        return

    total = sum(item['amount'] for item in expenses)
    highest = max(item['amount'] for item in expenses)
    lowest = min(item['amount'] for item in expenses)
    average = round(total / len(expenses), 2)

    print(f"Total Expenses: ₱{total:.2f}")
    print(f"Highest Expense: ₱{highest:.2f}")
    print(f"Lowest Expense: ₱{lowest:.2f}")
    print(f"Average Expense: ₱{average:.2f}")

    print("\nCategories Used:", ", ".join(sorted(used_categories)))


# ----------------------------
# Function: Delete Expense
# Lessons Used: Selection Structure, List Operations
# ----------------------------

def delete_expense():
    print("\n--- DELETE EXPENSE ---\n")

    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses()

    try:
        choice = int(input("\nEnter expense number to delete: "))
        if not (1 <= choice <= len(expenses)):
            print("Invalid selection.")
            return
    except ValueError:
        print("Invalid input.")
        return

    removed = expenses.pop(choice - 1)
    print(f"\nDeleted: ₱{removed['amount']:.2f} - {removed['category']}")


# ----------------------------
# MAIN MENU (While Loop)
# Lessons Used: While Loop, If/Elif/Else, Break, Continue
# ----------------------------

def main_menu():
    while True:  # Lesson 7: While Loop
        print("\n==============================")
        print("            MENU")
        print("==============================")
        print("[1] Add Expense")
        print("[2] View Expenses")
        print("[3] Summary Report")
        print("[4] Delete Expense")
        print("[5] Exit")
        
        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary_report()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            print("\nThank you for using Smart Budget Tracker!\n")
            break  # Lesson 7: Break
        else:
            print("Invalid choice! Try again.")
            continue  # Lesson 7: Continue


# Run Program
main_menu()

