#ALGORITHM
1. Start the program.
2. Input the employee's ID, name, basic pay, allowances, overtime hours, overtime rate, and incentives.
3. Validate that all salary components are non-negative.
4. Calculate overtime pay by multiplying overtime hours by the overtime rate.
5. Calculate gross salary:
   
   Gross Salary = Basic Pay + Allowances + Overtime Pay + Incentives
6. Calculate progressive deductions using these illustrative slabs:
   - First ₹10,000: 0% deduction.
   - Next ₹10,000: 5% deduction.
   - Amount above ₹20,000: 10% deduction.
7. Calculate net salary:
   
   Net Salary = Gross Salary − Total Deductions
8. Display the employee's salary statement in a formatted table.
9. Stop the program.

#FLOWCHART
                    START
                      |
                      v
             Enter Employee Details
                      |
                      v
          Enter Basic Pay, Allowances,
          Overtime Hours, Overtime Rate
                and Incentives
                      |
                      v
             Validate Salary Inputs
                      |
                      v
                Inputs Valid?
                /           \
              No             Yes
              |               |
              v               v
        Display Error    Calculate Overtime Pay
              |               |
              |               v
              |        Calculate Gross Salary
              |               |
              |               v
              |       Calculate Progressive
              |            Deductions
              |               |
              |               v
              |        Calculate Net Salary
              |               |
              |               v
              |       Generate Salary Statement
              |               |
              |               v
              |              STOP
              |
              +----> Re-enter Details


              #CODE
              
# File name: employee_payroll.py

def calculate_deduction(gross_salary):
    if gross_salary <= 10000:
        deduction = 0
    elif gross_salary <= 20000:
        deduction = (gross_salary - 10000) * 0.05
    else:
        deduction = (10000 * 0.05) + (
            (gross_salary - 20000) * 0.10
        )

    return deduction


def main():
    print("=== EMPLOYEE PAYROLL SYSTEM ===")

    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")

    try:
        basic_pay = float(input("Enter basic pay: Rs. "))
        allowances = float(input("Enter allowances: Rs. "))
        overtime_hours = float(input("Enter overtime hours: "))
        overtime_rate = float(input("Enter overtime rate per hour: Rs. "))
        incentives = float(input("Enter incentives: Rs. "))

        values = [
            basic_pay, allowances, overtime_hours,
            overtime_rate, incentives
        ]

        if any(value < 0 for value in values):
            print("Error: Values cannot be negative.")
            return

        overtime_pay = overtime_hours * overtime_rate

        gross_salary = (
            basic_pay + allowances + overtime_pay + incentives
        )

        deduction = calculate_deduction(gross_salary)
        net_salary = gross_salary - deduction

        print("\n========== SALARY STATEMENT ==========")
        print(f"Employee ID       : {emp_id}")
        print(f"Employee Name     : {name}")
        print("--------------------------------------")
        print(f"Basic Pay         : Rs. {basic_pay:.2f}")
        print(f"Allowances        : Rs. {allowances:.2f}")
        print(f"Overtime Pay      : Rs. {overtime_pay:.2f}")
        print(f"Incentives        : Rs. {incentives:.2f}")
        print("--------------------------------------")
        print(f"Gross Salary      : Rs. {gross_salary:.2f}")
        print(f"Total Deductions  : Rs. {deduction:.2f}")
        print("--------------------------------------")
        print(f"Net Salary        : Rs. {net_salary:.2f}")
        print("======================================")

    except ValueError:
        print("Error: Please enter valid numeric values.")


if __name__ == "__main__":
    main()

#OUTPUT

========== SALARY STATEMENT ==========
Employee ID       : E101
Employee Name     : Ravi
--------------------------------------
Basic Pay         : Rs. 15000.00
Allowances        : Rs. 3000.00
Overtime Pay      : Rs. 2000.00
Incentives        : Rs. 2000.00
--------------------------------------
Gross Salary      : Rs. 22000.00
Total Deductions  : Rs. 700.00
--------------------------------------
Net Salary        : Rs. 21300.00
======================================