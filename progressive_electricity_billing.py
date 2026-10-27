      #Algorithm
1. Start the program.
2. Define electricity rates for each consumption slab, fixed charges, surcharge percentage, rebate percentage, and unusual-increase threshold.
3. Input the number of months for which bills must be calculated.
4. For each month:
   - Input the month name and electricity consumption in units (kWh).
   - Calculate energy charges using progressive slabs.
   - Add fixed charges.
   - Calculate the surcharge on the applicable charges.
   - Apply the rebate to the subtotal.
   - Calculate the final electricity bill.
5. Store the monthly consumption and bill amount.
6. Compare each month's bill with the previous month's bill.
7. Calculate the percentage increase.
8. If the increase exceeds the predefined threshold of 30%, flag it as an unusual increase.
9. Display monthly bills, comparisons, and unusual-increase alerts.
10. Stop the program.

#FLOWCHART

                 START
                   |
                   v
      Define Slab Rates, Fixed Charges,
        Surcharge, Rebate and Threshold
                   |
                   v
         Input Number of Months
                   |
                   v
        Enter Month and Units Used
                   |
                   v
       Calculate Progressive Slab Charges
                   |
                   v
           Add Fixed Charges
                   |
                   v
       Calculate Surcharge and Rebate
                   |
                   v
         Calculate Final Bill Amount
                   |
                   v
          Store Monthly Bill Details
                   |
                   v
           More Months to Enter?
              /          \
            Yes           No
             |             |
             v             v
      Enter Next Month   Compare Monthly
                           Bills
                             |
                             v
                 Increase Greater Than 30%?
                       /           \
                     Yes            No
                      |              |
                      v              v
                Flag Unusual    Record Normal
                   Increase     Change
                      |              |
                      +------+-------+
                             |
                             v
                 Display Bills and Alerts
                             |
                             v
                            STOP

            #CODE
            
# File name: progressive_electricity_billing.py

SLAB1_LIMIT = 100
SLAB2_LIMIT = 200
SLAB3_LIMIT = 400

RATE1 = 2.00
RATE2 = 3.00
RATE3 = 4.50
RATE4 = 6.00

FIXED_CHARGE = 50.00
SURCHARGE_RATE = 0.05
REBATE_RATE = 0.05
UNUSUAL_INCREASE = 30.0


def calculate_energy_charge(units):
    if units <= 100:
        return units * RATE1
    elif units <= 200:
        return (100 * RATE1
                + (units - 100) * RATE2)
    elif units <= 400:
        return (100 * RATE1
                + 100 * RATE2
                + (units - 200) * RATE3)
    else:
        return (100 * RATE1
                + 100 * RATE2
                + 200 * RATE3
                + (units - 400) * RATE4)


def calculate_bill(units):
    energy_charge = calculate_energy_charge(units)
    fixed_charge = FIXED_CHARGE

    surcharge = (energy_charge + fixed_charge) * SURCHARGE_RATE

    # Rebate applies only when consumption is 100 units or less.
    rebate = energy_charge * REBATE_RATE if units <= 100 else 0

    total = energy_charge + fixed_charge + surcharge - rebate

    return energy_charge, surcharge, rebate, total


def main():
    bills = []
    n = int(input("Enter number of months: "))

    for i in range(n):
        print(f"\nMonth {i + 1}")
        month = input("Enter month name: ")
        units = float(input("Enter units consumed: "))

        if units < 0:
            print("Units cannot be negative.")
            return

        energy, surcharge, rebate, total = calculate_bill(units)

        bills.append({
            "month": month,
            "units": units,
            "energy": energy,
            "surcharge": surcharge,
            "rebate": rebate,
            "total": total
        })

    print("\n--- MONTHLY ELECTRICITY BILLS ---")
    print("Month      Units   Energy   Surcharge  Rebate   Total")

    for b in bills:
        print(
            f"{b['month']:<10} "
            f"{b['units']:<7.1f} "
            f"{b['energy']:<8.2f} "
            f"{b['surcharge']:<10.2f} "
            f"{b['rebate']:<8.2f} "
            f"{b['total']:.2f}"
        )

    print("\n--- MONTH-TO-MONTH COMPARISON ---")

    if len(bills) < 2:
        print("Enter at least two months to compare.")
    else:
        for i in range(1, len(bills)):
            previous = bills[i - 1]["total"]
            current = bills[i]["total"]

            if previous == 0:
                print(f"{bills[i]['month']}: Cannot calculate "
                      "percentage change from a zero bill.")
                continue

            change = ((current - previous) / previous) * 100

            print(
                f"{bills[i]['month']}: "
                f"{change:+.2f}% change from "
                f"{bills[i - 1]['month']}"
            )

            if change > UNUSUAL_INCREASE:
                print("  ALERT: Unusual bill increase detected!")
            else:
                print("  No unusual increase detected.")


if __name__ == "__main__":
    main()


#OUTPUT

--- MONTHLY ELECTRICITY BILLS ---
Month      Units   Energy   Surcharge  Rebate   Total
January    80.0    160.00   10.50      8.00     212.50
February   150.0   350.00   20.00      0.00     420.00
March      300.0   950.00   50.00      0.00     1050.00

--- MONTH-TO-MONTH COMPARISON ---
February: +97.65% change from January
  ALERT: Unusual bill increase detected!
March: +150.00% change from February
  ALERT: Unusual bill increase detected!