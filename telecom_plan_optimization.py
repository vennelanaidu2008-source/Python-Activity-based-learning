#ALGORITHM
1. Start the program.
2. Input the user's monthly data usage, call minutes, required validity days, and budget.
3. Define the available mobile plans with their prices, data limits, call limits, validity periods, and excess usage rates.
4. For each plan:
   - Calculate excess data charges if usage exceeds the plan's data allowance.
   - Calculate excess call charges if call minutes exceed the plan's allowance.
   - Calculate the total cost, including excess charges.
5. Check whether the plan satisfies the required validity and budget constraints.
6. Mark plans that satisfy all constraints as eligible.
7. Compare the total costs of all eligible plans.
8. Select the eligible plan with the lowest total cost.
9. Display the cost breakdown, eligibility status, and most economical plan.
10. If no plan is eligible, display an appropriate message.
11. Stop.

#FLOWCHART

                   START
                     |
                     v
           Input User Requirements
        (Data, Calls, Validity, Budget)
                     |
                     v
           Define Available Mobile Plans
                     |
                     v
              Select a Plan
                     |
                     v
          Calculate Excess Data Charges
                     |
                     v
          Calculate Excess Call Charges
                     |
                     v
             Calculate Total Cost
                     |
                     v
       Check Validity and Budget Constraints
                     |
                     v
                Plan Eligible?
                /           \
              Yes             No
               |               |
               v               v
        Store Eligible     Mark as Not
             Plan             Eligible
               |               |
               +-------+-------+
                       |
                       v
               Are More Plans Left?
                 /           \
               Yes            No
                |              |
                v              v
           Select Next    Any Eligible Plans?
              Plan          /          \
                           Yes           No
                            |             |
                            v             v
                     Find Lowest      Display No
                     Total Cost       Eligible Plan
                            |
                            v
                   Display Best Plan
                            |
                            v
                           STOP
    #CODE

    
# File name: telecom_plan_optimization.py

plans = [
    {
        "name": "Basic",
        "price": 199,
        "data": 2,
        "calls": 200,
        "validity": 28,
        "data_rate": 50,
        "call_rate": 0.50
    },
    {
        "name": "Smart",
        "price": 299,
        "data": 5,
        "calls": 500,
        "validity": 28,
        "data_rate": 40,
        "call_rate": 0.40
    },
    {
        "name": "Premium",
        "price": 399,
        "data": 10,
        "calls": 1000,
        "validity": 56,
        "data_rate": 30,
        "call_rate": 0.30
    },
    {
        "name": "Unlimited",
        "price": 499,
        "data": 20,
        "calls": 1500,
        "validity": 84,
        "data_rate": 20,
        "call_rate": 0.20
    }
]


def main():
    print("=== TELECOM PLAN OPTIMIZATION ===")

    try:
        data_used = float(input("Enter data usage (GB): "))
        calls_used = float(input("Enter call minutes used: "))
        required_validity = int(input("Enter required validity (days): "))
        budget = float(input("Enter budget (Rs.): "))

        if (data_used < 0 or calls_used < 0
                or required_validity <= 0 or budget < 0):
            print("Error: Enter valid non-negative usage and budget,")
            print("and a positive validity period.")
            return

        results = []

        for plan in plans:
            excess_data = max(0, data_used - plan["data"])
            excess_calls = max(0, calls_used - plan["calls"])

            data_charge = excess_data * plan["data_rate"]
            call_charge = excess_calls * plan["call_rate"]

            total_cost = (
                plan["price"] + data_charge + call_charge
            )

            eligible = (
                plan["validity"] >= required_validity
                and total_cost <= budget
            )

            results.append({
                "name": plan["name"],
                "base": plan["price"],
                "data_charge": data_charge,
                "call_charge": call_charge,
                "total": total_cost,
                "validity": plan["validity"],
                "eligible": eligible
            })

        print("\n--- PLAN COMPARISON ---")
        print("Plan       Base    DataExcess  CallExcess  Total   Status")

        for r in results:
            status = "Eligible" if r["eligible"] else "Not eligible"
            print(
                f"{r['name']:<10} "
                f"{r['base']:<7.2f} "
                f"{r['data_charge']:<11.2f} "
                f"{r['call_charge']:<11.2f} "
                f"{r['total']:<7.2f} "
                f"{status}"
            )

        eligible_plans = [
            r for r in results if r["eligible"]
        ]

        print("\n--- RECOMMENDATION ---")

        if eligible_plans:
            best = min(eligible_plans, key=lambda r: r["total"])

            print("Most economical plan:", best["name"])
            print(f"Base price: Rs. {best['base']:.2f}")
            print(f"Excess data charges: Rs. {best['data_charge']:.2f}")
            print(f"Excess call charges: Rs. {best['call_charge']:.2f}")
            print(f"Total cost: Rs. {best['total']:.2f}")
            print(f"Validity: {best['validity']} days")
        else:
            print("No plan satisfies both validity and budget constraints.")

    except ValueError:
        print("Error: Please enter valid numeric values.")


if __name__ == "__main__":
    main()

#OUTPUT
--- PLAN COMPARISON ---
Plan       Base    DataExcess  CallExcess  Total   Status
Basic      199.00  200.00      200.00      599.00  Not eligible
Smart      299.00  40.00       40.00       379.00  Eligible
Premium    399.00  0.00        0.00        399.00  Eligible
Unlimited  499.00  0.00        0.00        499.00  Not eligible

--- RECOMMENDATION ---
Most economical plan: Smart
Base price: Rs. 299.00
Excess data charges: Rs. 40.00
Excess call charges: Rs. 40.00
Total cost: Rs. 379.00
Validity: 28 days