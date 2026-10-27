#ALGORITHM
1. Start.
2. Read the travel budget in the base currency (INR).
3. Read the number of expense categories.
4. For each category, input the category name, expense amount in foreign currency, exchange rate, and conversion fee percentage.
5. Convert each expense into INR using the supplied exchange rate.
6. Calculate the conversion fee and add it to the converted expense.
7. Calculate the total travel expenditure.
8. Identify the largest expense category.
9. Compare total expenditure with the planned budget.
10. Display converted expenses, conversion fees, total expenditure, largest expense category, and budget status.
11. Stop.

#FLOWCHART
          +------------------+
          |      START       |
          +------------------+
                   |
                   v
          +------------------+
          | Input travel     |
          | budget in INR    |
          +------------------+
                   |
                   v
          +------------------+
          | Input number of  |
          | expense categories|
          +------------------+
                   |
                   v
          +------------------+
          | Input category,  |
          | foreign amount,  |
          | exchange rate,   |
          | fee percentage   |
          +------------------+
                   |
                   v
          +------------------+
          | Convert amount   |
          | to INR           |
          +------------------+
                   |
                   v
          +------------------+
          | Calculate fee    |
          | and final cost   |
          +------------------+
                   |
                   v
          +------------------+
          | Store category   |
          | cost and update  |
          | total expenditure|
          +------------------+
                   |
                   v
          +------------------+
          | More categories? |
          +------------------+
             | Yes       | No
             |           v
             |   +------------------+
             |   | Find largest     |
             |   | expense category |
             |   +------------------+
             |           |
             |           v
             |   +------------------+
             |   | Compare total    |
             |   | with budget      |
             |   +------------------+
             |           |
             |           v
             |   +------------------+
             |   | Display report   |
             |   +------------------+
             |           |
             |           v
             |   +------------------+
             |   |       STOP       |
             |   +------------------+
             |
             +----> Input next category

             #CODE
             
# Filename: multi_currency_travel_budget.py

print("MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")

budget = float(input("Enter travel budget in INR: "))
n = int(input("Enter number of expense categories: "))

expenses = []
total_expense = 0.0

for i in range(n):
    print(f"\nExpense Category {i + 1}")

    category = input("Enter category name: ")
    amount = float(input("Enter expense amount in foreign currency: "))
    rate = float(input("Enter exchange rate (INR per unit): "))
    fee_percent = float(input("Enter conversion fee percentage: "))

    converted_amount = amount * rate
    conversion_fee = converted_amount * fee_percent / 100
    final_cost = converted_amount + conversion_fee

    expenses.append((category, converted_amount,
                     conversion_fee, final_cost))
    total_expense += final_cost

print("\n----- TRAVEL EXPENSE REPORT -----")
print(f"{'Category':<15}{'Converted (INR)':>18}"
      f"{'Fee (INR)':>12}{'Total (INR)':>15}")

for category, converted, fee, cost in expenses:
    print(f"{category:<15}{converted:>18.2f}"
          f"{fee:>12.2f}{cost:>15.2f}")

if expenses:
    largest = max(expenses, key=lambda item: item[3])
    print(f"\nLargest expense category: {largest[0]}")
    print(f"Largest category cost: INR {largest[3]:.2f}")
else:
    print("\nNo expense categories entered.")

print(f"Total expenditure: INR {total_expense:.2f}")
print(f"Travel budget: INR {budget:.2f}")
print(f"Remaining budget: INR {budget - total_expense:.2f}")

if total_expense > budget:
    print("Budget Status: OVER BUDGET")
elif total_expense < budget:
    print("Budget Status: WITHIN BUDGET")
else:
    print("Budget Status: EXACTLY ON BUDGET")

#OUTPUT
MULTI-CURRENCY TRAVEL BUDGET ANALYSIS

----- TRAVEL EXPENSE REPORT -----
Category          Converted (INR)   Fee (INR)    Total (INR)
Hotel                   18000.00      360.00       18360.00
Food                     9000.00       90.00        9090.00
Transport               13500.00      202.50       13702.50

Largest expense category: Hotel
Largest category cost: INR 18360.00
Total expenditure: INR 41152.50
Travel budget: INR 50000.00
Remaining budget: INR 8847.50
Budget Status: WITHIN BUDGET